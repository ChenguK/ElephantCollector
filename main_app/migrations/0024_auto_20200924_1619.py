# Generated by Django 3.1.1 on 2020-09-24 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0023_elephant_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elephant',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]