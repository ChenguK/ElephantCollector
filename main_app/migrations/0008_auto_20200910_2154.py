# Generated by Django 3.1 on 2020-09-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200910_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elephant',
            name='dob',
            field=models.DateField(verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='elephant',
            name='dod',
            field=models.DateField(verbose_name='date of death'),
        ),
    ]
