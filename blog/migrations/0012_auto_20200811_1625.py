# Generated by Django 3.0.8 on 2020-08-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200811_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
    ]
