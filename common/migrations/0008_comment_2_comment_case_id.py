# Generated by Django 2.0.2 on 2018-03-05 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20180306_0036'),
        ('common', '0007_comment_2_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_2_comment',
            name='case_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case', to='questions.Case'),
        ),
    ]
