# Generated by Django 5.0.6 on 2024-06-25 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_computer_comptype_alter_computer_cpu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='computer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.computer'),
        ),
    ]
