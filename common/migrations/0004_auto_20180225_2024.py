# Generated by Django 2.0.2 on 2018-02-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20180224_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ppa_percent',
            field=models.CharField(default='0', max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='secondary_practice_area',
            field=models.CharField(choices=[('AUTO', 'AUTO'), ('GENERAL', 'GENERAL'), ('BAD FAITH', 'BAD FAITH'), ('CRIMINAL', 'CRIMINAL'), ('MEDICAL MALPRACTICE', 'MEDICAL MALPRACTICE'), ('NURSING HOME', 'NURSING HOME'), ('PREMISES', 'PREMISES'), ('PROPERTY INS', 'PROPERTY INS')], default='NA', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='spa_percent',
            field=models.CharField(default='0', max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_practice_area',
            field=models.CharField(choices=[('AUTO', 'AUTO'), ('GENERAL', 'GENERAL'), ('BAD FAITH', 'BAD FAITH'), ('CRIMINAL', 'CRIMINAL'), ('MEDICAL MALPRACTICE', 'MEDICAL MALPRACTICE'), ('NURSING HOME', 'NURSING HOME'), ('PREMISES', 'PREMISES'), ('PROPERTY INS', 'PROPERTY INS')], default='NA', max_length=64),
        ),
    ]
