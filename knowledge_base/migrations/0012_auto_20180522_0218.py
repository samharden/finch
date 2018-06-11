# Generated by Django 2.0.4 on 2018-05-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0011_auto_20180519_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kb_item',
            options={'ordering': ['kb_type']},
        ),
        migrations.AlterField(
            model_name='kb_item',
            name='aff_resp',
            field=models.CharField(default='', max_length=600, verbose_name='If Affirmate Response to Trigger'),
        ),
        migrations.AlterField(
            model_name='kb_item',
            name='kb_type',
            field=models.CharField(choices=[('guide', 'Practice Guide'), ('statute', 'Statute'), ('element', 'Element'), ('grounds', 'Grounds')], max_length=64, verbose_name='Type of Item'),
        ),
    ]
