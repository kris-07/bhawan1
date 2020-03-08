# Generated by Django 3.0.3 on 2020-03-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restswitch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='d1',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='d2',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='d3',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='d4',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='d5',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s1',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s10',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s2',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s3',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s4',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s5',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s6',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s7',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s8',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='s9',
            field=models.BooleanField(default=None, null=True),
        ),
    ]