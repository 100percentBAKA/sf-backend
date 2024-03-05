# Generated by Django 5.0.2 on 2024-03-04 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image_url', models.CharField(default='/no-url', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image_url', models.CharField(default='/no-url', max_length=500)),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='endpoints.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image_url', models.CharField(default='/no-image-url', max_length=500)),
                ('document_url', models.CharField(default='/no-doc-url', max_length=500)),
                ('sub_category', models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='endpoints.subcategory')),
            ],
        ),
    ]