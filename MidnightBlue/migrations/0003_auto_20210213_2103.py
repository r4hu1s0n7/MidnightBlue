# Generated by Django 3.1.5 on 2021-02-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidnightBlue', '0002_auto_20210213_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedb',
            name='release_date',
            field=models.CharField(max_length=50),
        ),
    ]
