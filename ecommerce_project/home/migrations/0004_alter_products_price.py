# Generated by Django 3.2.15 on 2022-08-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220825_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]