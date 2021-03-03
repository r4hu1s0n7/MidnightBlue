# Generated by Django 3.1.5 on 2021-02-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=500)),
                ('original_title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=1000)),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField()),
                ('runtime', models.FloatField()),
                ('tagline', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
                ('cast', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('poster', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'MovieDB',
            },
        ),
    ]
