# Generated by Django 3.2 on 2021-04-20 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='')),
                ('phone', models.CharField(max_length=11)),
                ('description', models.CharField(max_length=200)),
                ('store_name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
