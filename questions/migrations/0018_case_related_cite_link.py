# Generated by Django 2.0.4 on 2018-04-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_auto_20180416_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='related_cite_link',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
