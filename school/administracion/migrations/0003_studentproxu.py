# Generated by Django 4.1.3 on 2022-11-30 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_classroom_table_alter_student_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProxu',
            fields=[
            ],
            options={
                'ordering': ['-id'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.student',),
        ),
    ]
