# Generated by Django 3.2.3 on 2021-06-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_news_nnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='nnews',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
