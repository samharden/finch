# Generated by Django 2.0.4 on 2018-05-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20180518_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('AL', 'AL'), ('CA', 'CA'), ('FL', 'FL'), ('GA', 'GA'), ('KY', 'KY'), ('IL', 'IL'), ('MS', 'MS'), ('NY', 'NY'), ('NC', 'NC'), ('SC', 'SC'), ('TN', 'TN'), ('TX', 'TX')], max_length=64),
        ),
    ]
