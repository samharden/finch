# Generated by Django 2.0.2 on 2018-02-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20180228_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='issue_detail',
            field=models.CharField(max_length=10000, verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='case',
            name='rel_statute_link',
            field=models.CharField(max_length=150, verbose_name='Statute Link'),
        ),
    ]
