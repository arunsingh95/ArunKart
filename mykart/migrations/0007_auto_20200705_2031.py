# Generated by Django 2.2 on 2020-07-05 15:01

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mykart', '0006_auto_20200705_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product_image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='product_image'),
        ),
    ]
