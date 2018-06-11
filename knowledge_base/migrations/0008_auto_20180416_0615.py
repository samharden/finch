# Generated by Django 2.0.4 on 2018-04-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0007_auto_20180411_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kb_item',
            name='kb_type',
            field=models.CharField(choices=[('pleadings', 'Pleading'), ('discovery', 'Discovery'), ('motions', 'Motion'), ('orders', 'Order'), ('deposition', 'Deposition'), ('statute', 'Statute'), ('caselaw', 'Caselaw')], max_length=64),
        ),
    ]
