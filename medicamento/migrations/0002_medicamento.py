# Generated by Django 4.1.4 on 2022-12-21 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Medicamento')),
                ('nombre_medicamento', models.CharField(max_length=100, verbose_name='Nombre Medicamento')),
                ('medida_medicamento', models.IntegerField(verbose_name='Medida Medicamento')),
                ('cantidad_comprimidos', models.IntegerField(verbose_name='Cantidad Medicamento')),
                ('forma_farmaceutica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.forma_farmaceutica', verbose_name='Forma_farmaceutica')),
                ('laboratorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.laboratorio', verbose_name='Laboratorio')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.marca', verbose_name='Marca')),
                ('recomendacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.recomendacion_consumo', verbose_name='Recomendacion_consumo')),
                ('tipo_farmaco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.tipo_farmaco', verbose_name='Tipo_farmaco')),
                ('via_ingesta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.via_ingesta', verbose_name='Via_ingesta')),
            ],
            options={
                'ordering': ['-laboratorio'],
            },
        ),
    ]
