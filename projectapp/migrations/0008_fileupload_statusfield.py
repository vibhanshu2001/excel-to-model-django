# Generated by Django 3.2 on 2021-04-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0007_remove_fileupload_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='statusfield',
            field=models.BooleanField(default=False),
        ),
    ]