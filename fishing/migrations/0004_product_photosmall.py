# Generated by Django 3.1.2 on 2020-11-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0003_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photosmall',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
