# Generated by Django 3.0.8 on 2020-07-29 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200728_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='second_text',
        ),
    ]
