# Generated by Django 3.2.5 on 2022-05-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
