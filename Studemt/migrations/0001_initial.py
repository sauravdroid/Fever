# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 03:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('second_pref', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('category', models.CharField(choices=[('sc', 'S.C'), ('gen', 'General'), ('st', 'S.T'), ('obc-a', 'O.B.C-A'), ('obc-b', 'O.B.C-B')], max_length=255)),
                ('domcile_wb', models.BooleanField()),
                ('contact_number', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('rank', models.IntegerField()),
                ('year_of_passing', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=255)),
                ('availability', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='hello',
            name='first_pref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first', to='Studemt.Subject'),
        ),
        migrations.AddField(
            model_name='hello',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
