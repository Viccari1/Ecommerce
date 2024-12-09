# Generated by Django 5.1.4 on 2024-12-08 21:18

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[users.validators.validate_cpf]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[users.validators.validate_password]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[users.validators.validate_phone]),
        ),
    ]