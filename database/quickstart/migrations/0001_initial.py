# Generated by Django 2.0 on 2017-12-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20, unique=True)),
                ('subject', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
