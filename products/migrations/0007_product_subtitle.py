# Generated by Django 3.2.21 on 2023-10-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
