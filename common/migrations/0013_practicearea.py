# Generated by Django 2.0.4 on 2018-05-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_casetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practicearea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=1000)),
            ],
        ),
    ]
