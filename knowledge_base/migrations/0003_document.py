# Generated by Django 2.0.2 on 2018-03-01 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0002_auto_20180224_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('practice_area', models.CharField(choices=[('AUTO', 'AUTO'), ('GENERAL', 'GENERAL'), ('BAD FAITH', 'BAD FAITH'), ('CRIMINAL', 'CRIMINAL'), ('MEDICAL MALPRACTICE', 'MEDICAL MALPRACTICE'), ('NURSING HOME', 'NURSING HOME'), ('PREMISES', 'PREMISES'), ('PROPERTY INS', 'PROPERTY INS')], max_length=64)),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('body', models.CharField(max_length=60000, verbose_name='Body')),
            ],
        ),
    ]
