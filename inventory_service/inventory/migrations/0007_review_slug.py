# Generated by Django 4.0 on 2022-11-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.CharField(default=None, max_length=80),
        ),
    ]
