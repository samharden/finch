# Generated by Django 2.0.4 on 2018-04-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0005_auto_20180306_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='kb_item',
            name='state',
            field=models.CharField(choices=[('AL', 'AL'), ('FL', 'FL'), ('GA', 'GA')], default='FL', max_length=64),
        ),
    ]
