# Generated by Django 2.0.4 on 2018-06-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20180614_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='primary_practice_area',
            field=models.CharField(choices=[('GENERAL', 'GENERAL'), ('COMPLAINT', 'COMPLAINT'), ('ANSWER', 'ANSWER'), ('AFFIRMATIVE DEFENSES', 'AFFIRMATIVE DEFENSES'), ('COURT PROCEDURE', 'COURT PROCEDURE'), ('JUDGE PREFERENCE', 'JUDGE PREFERENCE')], default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='secondary_practice_area',
            field=models.CharField(choices=[('GENERAL', 'GENERAL'), ('COMPLAINT', 'COMPLAINT'), ('ANSWER', 'ANSWER'), ('AFFIRMATIVE DEFENSES', 'AFFIRMATIVE DEFENSES'), ('COURT PROCEDURE', 'COURT PROCEDURE'), ('JUDGE PREFERENCE', 'JUDGE PREFERENCE')], default='NA', max_length=64),
        ),
    ]
