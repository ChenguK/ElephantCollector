# Generated by Django 3.1.1 on 2020-09-25 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_trainer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='user',
        ),
    ]