# Generated by Django 3.1 on 2020-09-10 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200909_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elephant',
            name='image',
            field=models.ImageField(upload_to='main_app/images/'),
        ),
    ]
