# Generated by Django 4.1.4 on 2022-12-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_enfermera_whatsaap_enfermera'),
    ]

    operations = [
        migrations.AddField(
            model_name='preregistro',
            name='terminos_uso',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
