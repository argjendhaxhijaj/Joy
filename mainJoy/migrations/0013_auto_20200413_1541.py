# Generated by Django 3.0.3 on 2020-04-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainJoy', '0012_njoftimet_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='njoftimet',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='njoftimet',
            name='url',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
