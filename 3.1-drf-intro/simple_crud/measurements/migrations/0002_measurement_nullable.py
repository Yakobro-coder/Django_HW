# Generated by Django 3.2.8 on 2021-11-05 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='nullable',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
