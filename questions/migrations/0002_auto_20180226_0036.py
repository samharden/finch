# Generated by Django 2.0.2 on 2018-02-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='related_statute',
        ),
        migrations.AddField(
            model_name='case',
            name='related_document_name',
            field=models.CharField(default='Doc Name', max_length=64, verbose_name='Upload Name'),
            preserve_default=False,
        ),
    ]
