# Generated by Django 4.0.1 on 2022-05-01 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gen_task', '0004_members_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['started_at']},
        ),
    ]
