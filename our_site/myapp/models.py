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

