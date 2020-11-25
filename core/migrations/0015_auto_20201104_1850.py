# Generated by Django 2.2.8 on 2020-11-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]