# Generated by Django 3.2.8 on 2021-10-24 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['tag__name']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
    ]
