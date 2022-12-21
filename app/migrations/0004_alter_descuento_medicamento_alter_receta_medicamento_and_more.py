# Generated by Django 4.1.4 on 2022-12-21 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0002_medicamento'),
        ('app', '0003_alter_medicamento_forma_farmaceutica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='medicamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.medicamento', verbose_name='Medicamento'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='medicamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.medicamento', verbose_name='Medicamento'),
        ),
        migrations.DeleteModel(
            name='Medicamento',
        ),
    ]
