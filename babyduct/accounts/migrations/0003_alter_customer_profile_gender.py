# Generated by Django 4.0 on 2022-11-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6),
        ),
    ]
