# Generated by Django 4.1.3 on 2022-11-30 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_studentproxu'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.teacher',),
        ),
    ]
