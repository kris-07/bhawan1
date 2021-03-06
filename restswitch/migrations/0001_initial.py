# Generated by Django 3.0.3 on 2020-03-24 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', jsonfield.fields.JSONField(default=dict)),
                ('s1', models.NullBooleanField(default=None)),
                ('s2', models.NullBooleanField(default=None)),
                ('s3', models.NullBooleanField(default=None)),
                ('s4', models.NullBooleanField(default=None)),
                ('s5', models.NullBooleanField(default=None)),
                ('s6', models.NullBooleanField(default=None)),
                ('s7', models.NullBooleanField(default=None)),
                ('s8', models.NullBooleanField(default=None)),
                ('s9', models.NullBooleanField(default=None)),
                ('s10', models.NullBooleanField(default=None)),
                ('d1', models.PositiveSmallIntegerField(default=None, null=True)),
                ('d2', models.PositiveSmallIntegerField(default=None, null=True)),
                ('d3', models.PositiveSmallIntegerField(default=None, null=True)),
                ('d4', models.PositiveSmallIntegerField(default=None, null=True)),
                ('d5', models.PositiveSmallIntegerField(default=None, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
