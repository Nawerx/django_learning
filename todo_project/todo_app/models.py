from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    class Meta:
        db_table = "users"


class Note(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

    finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        MyUser, db_column="author_id", related_name="notes", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "notes"
