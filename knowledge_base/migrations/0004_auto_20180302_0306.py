# Generated by Django 2.0.2 on 2018-03-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0003_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='KB_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kb_type', models.CharField(default='statute', max_length=64, verbose_name='Type')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('chapter', models.CharField(max_length=64, verbose_name='Title')),
                ('heading', models.CharField(max_length=64, verbose_name='Heading')),
                ('statute_number', models.CharField(max_length=64, verbose_name='Related Statute')),
                ('statute_body', models.CharField(max_length=60000, verbose_name='Body')),
            ],
        ),
        migrations.DeleteModel(
            name='Statute',
        ),
    ]
