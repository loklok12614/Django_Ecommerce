# Generated by Django 2.2.8 on 2021-05-26 19:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20210526_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[300, 500], upload_to=''),
        ),
    ]
