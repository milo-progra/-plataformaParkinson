# Generated by Django 4.1.4 on 2022-12-20 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.tipo_usuario', verbose_name='Tipo Usuario'),
        ),
    ]
