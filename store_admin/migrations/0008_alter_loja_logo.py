# Generated by Django 5.1.4 on 2024-12-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_admin', '0007_loja_email_loja_endereco_loja_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='logo',
            field=models.ImageField(max_length=255, null=True, upload_to='static/media/logos'),
        ),
    ]
