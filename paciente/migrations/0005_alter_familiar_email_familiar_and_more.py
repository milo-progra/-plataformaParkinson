# Generated by Django 4.1.4 on 2023-02-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_alter_familiar_email_familiar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='email_familiar',
            field=models.CharField(max_length=100, unique=True, verbose_name='Email Familiar'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='rut_familiar',
            field=models.CharField(max_length=10, unique=True, verbose_name='Rut Familiar'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='telegram_familiar',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Telegram Familiar'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email_paciente',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rut_paciente',
            field=models.CharField(max_length=10, unique=True, verbose_name='Rut Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telegram_paciente',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Telegram Paciente'),
        ),
    ]
