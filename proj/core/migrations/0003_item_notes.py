# Generated by Django 3.0.1 on 2020-01-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='notes',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
