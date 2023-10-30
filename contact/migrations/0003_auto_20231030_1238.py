# Generated by Django 3.2.21 on 2023-10-30 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20231030_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('Courses for schools/education', 'Courses for schools/education'), ('Pricing Inquiry', 'Pricing Inquiry'), ('Business Inquiry', 'Business Inquiry'), ('Trouble using the site', 'Trouble using the site'), ('Trouble accessing my course', 'Trouble accessing my course'), ('Account Issues', 'Account Issues'), ('Other', 'Other')], max_length=254),
        ),
    ]