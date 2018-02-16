# Generated by Django 2.0.2 on 2018-02-16 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mundialitisapps', '0007_auto_20180213_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('puntaje', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Players',
                'verbose_name': 'Player',
            },
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
        ),
        migrations.AddField(
            model_name='players',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundialitisapps.teams'),
        ),
    ]
