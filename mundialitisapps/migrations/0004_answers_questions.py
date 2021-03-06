# Generated by Django 2.0.2 on 2018-02-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundialitisapps', '0003_auto_20180211_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
