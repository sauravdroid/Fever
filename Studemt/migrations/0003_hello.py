# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 03:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Studemt', '0002_auto_20160920_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('second_pref', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('first_pref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first', to='Studemt.Subject')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]