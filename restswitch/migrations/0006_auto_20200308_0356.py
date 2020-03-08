# Generated by Django 3.0.3 on 2020-03-07 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restswitch', '0005_auto_20200308_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]