# Generated by Django 3.2.3 on 2021-06-08 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_nnews_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nnews',
            old_name='photo',
            new_name='image',
        ),
    ]
