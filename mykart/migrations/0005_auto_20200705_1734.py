# Generated by Django 2.2 on 2020-07-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mykart', '0004_auto_20200619_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
