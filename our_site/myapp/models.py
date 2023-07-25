import django.contrib.auth.models
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_email
from django.db import models
from django.utils.timezone import datetime

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=32, verbose_name="Назва")
    content = models.TextField(null=False, verbose_name="Контент")
    created_as = models.DateTimeField(null=False, default=datetime.now)

    class Meta:
        managed = True
        db_table = "notes"
        verbose_name = "Замітку"
        verbose_name_plural = "Замітки"

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True, validators=[MinLengthValidator(4), MaxLengthValidator(32)])
    password = models.TextField(validators=[MinLengthValidator(8), MaxLengthValidator(32)])
    email = models.CharField(validators=[validate_email])

    class Meta:
        managed = True
        db_table = "users"

