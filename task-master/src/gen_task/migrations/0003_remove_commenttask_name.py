# Generated by Django 4.0.1 on 2022-04-20 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gen_task', '0002_correction_task_and_check_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commenttask',
            name='name',
        ),
    ]