# Generated by Django 3.2.21 on 2023-10-19 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20231019_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_basket',
        ),
    ]