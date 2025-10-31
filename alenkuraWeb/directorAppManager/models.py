from django.db import models
from django.conf import settings
from coreBD.models import DateTime
# Create your models here.


class Docent(DateTime):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )

    phone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.name}"