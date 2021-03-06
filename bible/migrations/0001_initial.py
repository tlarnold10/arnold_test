# Generated by Django 2.1.4 on 2019-01-17 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=25)),
                ('chapter', models.IntegerField()),
                ('verses', models.CharField(max_length=10)),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=25)),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.Emotion')),
            ],
            options={
                'ordering': ['book'],
            },
        ),
    ]
