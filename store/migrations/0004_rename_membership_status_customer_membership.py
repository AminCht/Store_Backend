# Generated by Django 4.0.6 on 2022-07-20 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='membership_status',
            new_name='membership',
        ),
    ]
