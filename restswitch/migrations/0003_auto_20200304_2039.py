# Generated by Django 3.0.3 on 2020-03-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restswitch', '0002_auto_20200304_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='s1',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s10',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s2',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s3',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s4',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s5',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s6',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s7',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s8',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s9',
            field=models.NullBooleanField(default=None),
        ),
    ]