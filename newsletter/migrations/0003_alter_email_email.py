# Generated by Django 3.2.21 on 2023-10-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20231024_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email is already subscribed.'}, max_length=254, unique=True),
        ),
    ]
