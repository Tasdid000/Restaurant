# Generated by Django 4.0.5 on 2022-06-13 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapi', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]