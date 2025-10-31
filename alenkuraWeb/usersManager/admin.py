from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from coreBD.models import Rol
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User
# Register your models here.

class UserCreation(forms.ModelForm):
    name = forms.CharField(label="Username", widget=forms.TextInput)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    rol = forms.ModelChoiceField(label="Rol", queryset=Rol.objects.all())

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChange(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'is_admin', 'is_docent', 'is_director', 'is_active']

class UserAdmin(BaseUserAdmin):
    readonly_fields = ['createdAt', 'updatedAt']

    form = UserChange
    add_form = UserCreation

    #Muestra los campos en la tabla de usuarios de la tabla User
    list_display = ['name', 'email', 'is_docent', 'is_director', 'is_admin', 'rol']

    #Muestra una lista para los filtros
    list_filter = ['is_admin', 'rol']

    #Esto es lo que aparece al modificar
    fieldsets = [
        (None, {"fields": ['name', 'email', 'password']}),
        ('Permisos', {'fields': ['is_admin', 'is_docent', 'is_director', 'is_active']}),
    ]

    #Aquí se mostrarán los campos para el formulario de creación de usuarios en admin
    add_fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['name', 'email', 'password1', 'password2', 'rol'],
            },
        ),
    ]

    def is_staff(self, obj):
        return obj.is_admin
    is_staff.boolean = True


    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
