# Generated by Django 2.2.3 on 2020-05-29 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200516_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisposeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disposer', models.CharField(max_length=100)),
                ('create_time', models.DateField(default=django.utils.timezone.now)),
                ('eventID', models.CharField(default=0, max_length=100)),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='PostRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=100)),
                ('create_time', models.DateField(default=django.utils.timezone.now)),
                ('eventID', models.CharField(default=0, max_length=100)),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
    ]