# Generated by Django 3.2.25 on 2024-08-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_merge_20240820_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
