# Generated by Django 4.0.1 on 2022-07-22 08:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_task', '0011_next_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, default=list, null=True, size=20, verbose_name='Отвественные'),
        ),
    ]