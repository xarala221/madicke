# Generated by Django 2.1.4 on 2019-01-08 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190105_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='equipement',
            field=models.ImageField(blank=True, null=True, upload_to='equipements'),
        ),
    ]