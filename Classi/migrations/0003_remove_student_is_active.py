# Generated by Django 4.1 on 2023-01-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classi', '0002_student_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
    ]
