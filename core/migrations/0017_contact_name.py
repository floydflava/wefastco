# Generated by Django 3.0.5 on 2022-07-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220707_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
