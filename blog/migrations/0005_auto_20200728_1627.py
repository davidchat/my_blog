# Generated by Django 3.0.8 on 2020-07-28 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200728_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]
