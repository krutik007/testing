# Generated by Django 2.1.4 on 2019-03-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('srollno', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sname', models.TextField()),
                ('scity', models.CharField(max_length=50)),
            ],
        ),
    ]
