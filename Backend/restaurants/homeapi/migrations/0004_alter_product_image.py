# Generated by Django 4.0.5 on 2022-06-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapi', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='restaurants/images'),
        ),
    ]
