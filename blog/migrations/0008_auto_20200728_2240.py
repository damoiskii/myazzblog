# Generated by Django 3.0.8 on 2020-07-29 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200728_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='first_text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='second_text',
            new_name='intro_content',
        ),
    ]
