# Generated by Django 3.1.7 on 2021-03-29 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='editor',
        ),
    ]