# Generated by Django 3.1 on 2020-09-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elephant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=50)),
                ('fictional', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('dod', models.CharField(max_length=50)),
                ('wikilink', models.URLField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('note', models.TextField(max_length=300)),
            ],
        ),
    ]
