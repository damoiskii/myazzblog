# Generated by Django 3.0.8 on 2020-07-27 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
