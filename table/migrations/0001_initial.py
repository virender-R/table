# Generated by Django 4.2.3 on 2023-07-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='storedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=250)),
                ('second', models.CharField(max_length=250)),
                ('result', models.CharField(max_length=250)),
            ],
        ),
    ]
