# Generated by Django 3.1 on 2022-06-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220526_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
