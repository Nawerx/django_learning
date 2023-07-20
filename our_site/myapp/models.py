import django.contrib.auth.models
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_email
from django.db import models
from django.utils.timezone import datetime

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=32)
    content = models.TextField(null=False)
    created_as = models.DateTimeField(null=False, default=datetime.now)

    class Meta:
        managed = True
        db_table = "notes"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True, validators=[MinLengthValidator(4), MaxLengthValidator(32)])
    password = models.TextField(validators=[MinLengthValidator(8), MaxLengthValidator(32)]) #hash найти!!!
    email = models.CharField(validators=[validate_email])

    class Meta:
        managed = True
        db_table = "users"