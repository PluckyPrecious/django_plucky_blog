# Generated by Django 3.1.8 on 2021-05-07 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pluckyblog', '0008_auto_20210507_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_connected',
        ),
    ]