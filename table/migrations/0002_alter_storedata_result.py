# Generated by Django 4.2.3 on 2023-07-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='result',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
