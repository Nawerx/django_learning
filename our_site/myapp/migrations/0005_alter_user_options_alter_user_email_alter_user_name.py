# Generated by Django 4.2.3 on 2023-07-28 01:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_note_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': 'Користувача', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(validators=[django.core.validators.EmailValidator()], verbose_name='Пошта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(unique=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(32)], verbose_name='Користувач'),
        ),
    ]