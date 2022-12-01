# Generated by Django 4.1.3 on 2022-11-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_rename_lastt_name_student_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
                ('Curso', models.CharField(max_length=30)),
                ('Evaluador', models.CharField(max_length=50)),
                ('Duracion', models.IntegerField()),
                ('Preguntas', models.IntegerField()),
                ('Puntaje_total', models.IntegerField()),
            ],
            options={
                'db_table': 'Examen_Final',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
                ('Curso', models.CharField(max_length=30)),
                ('Evaluador', models.CharField(max_length=50)),
                ('Tema', models.CharField(max_length=100)),
                ('Grupos', models.IntegerField()),
            ],
            options={
                'db_table': 'Proyecto',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='born_date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='born_date',
            field=models.DateField(default=''),
        ),
        migrations.CreateModel(
            name='ProyectoProxy',
            fields=[
            ],
            options={
                'ordering': ['Tema'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.proyecto',),
        ),
    ]