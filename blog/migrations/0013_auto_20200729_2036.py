# Generated by Django 3.0.8 on 2020-07-30 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200729_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_tags',
            field=models.CharField(choices=[('travel', 'Travel'), ('fashion', 'Fashion'), ('technology', 'Technology'), ('food', 'Food'), ('photography', 'Photography')], max_length=20, null=True),
        ),
    ]
