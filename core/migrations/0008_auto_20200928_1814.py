# Generated by Django 2.2.8 on 2020-09-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200928_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]