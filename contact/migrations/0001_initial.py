# Generated by Django 3.2.21 on 2023-10-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('1', 'Courses for schools/education'), ('2', 'Pricing Inquiry'), ('3', 'Business Inquiry'), ('4', 'Trouble using the site'), ('5', 'Trouble accessing my course'), ('6', 'Recover my account'), ('7', 'Other')], max_length=254)),
                ('message', models.TextField(max_length=1024)),
            ],
        ),
    ]
