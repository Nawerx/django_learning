from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_email
from django.db import models
from django.urls import reverse


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=32, verbose_name="Назва")
    content = models.TextField(null=False, verbose_name="Контент")
    created_at = models.DateTimeField(null=False, auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Змінено")

    class Meta:
        managed = True
        db_table = "notes"
        verbose_name = "Замітку"
        verbose_name_plural = "Замітки"

    def get_absolute_url(self):
        return reverse("show_note", kwargs={'id': self.id})


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True, validators=[MinLengthValidator(4), MaxLengthValidator(32)],
                            verbose_name="Користувач")

    password = models.TextField(validators=[MinLengthValidator(8), MaxLengthValidator(32)])
    email = models.CharField(validators=[validate_email], verbose_name="Пошта")

    class Meta:
        managed = True
        db_table = "users"
        verbose_name = "Користувача"
        verbose_name_plural = "Користувачі"

    def get_absolute_url(self):
        return reverse("show_user", kwargs={'id': self.id})







