# Generated by Django 2.0.4 on 2018-06-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_kbtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casetype',
            name='type',
            field=models.CharField(max_length=1000, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='kbtype',
            name='kb_type',
            field=models.CharField(max_length=1000, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='area',
            field=models.CharField(max_length=1000, verbose_name='Area'),
        ),
    ]
