# Generated by Django 4.1.4 on 2022-12-21 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_institucion', models.CharField(max_length=100, verbose_name='Nombre Institución')),
                ('descripcion', models.CharField(max_length=2000, verbose_name='Descripción Institución')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comuna', verbose_name='Comuna')),
            ],
        ),
    ]
