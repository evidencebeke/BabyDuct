# Generated by Django 4.0 on 2022-11-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_product_slug_review_date_alter_productsimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=80),
        ),
    ]
