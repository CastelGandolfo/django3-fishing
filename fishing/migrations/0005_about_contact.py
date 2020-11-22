# Generated by Django 3.1.2 on 2020-11-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0004_product_photosmall'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('adres', models.CharField(blank=True, max_length=100)),
                ('mail', models.CharField(blank=True, max_length=100)),
                ('nip', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]