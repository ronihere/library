# Generated by Django 3.2.5 on 2022-05-01 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0012_review_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]
