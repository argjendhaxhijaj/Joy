# Generated by Django 3.0.3 on 2020-04-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainJoy', '0007_auto_20200408_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='njoftimet',
            name='first_name',
            field=models.CharField(blank='False', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='njoftimet',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
