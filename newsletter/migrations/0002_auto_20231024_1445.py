# Generated by Django 3.2.21 on 2023-10-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='Email',
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name_plural': 'Email Addresses'},
        ),
    ]