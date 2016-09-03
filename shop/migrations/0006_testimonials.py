# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_programs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to='image_pic', verbose_name='Image')),
                ('testimonial', models.TextField(blank=True, help_text='Testimonial')),
            ],
        ),
    ]