# Generated by Django 3.0.8 on 2020-08-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200809_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='timeline_photo/%Y/%m/%d'),
        ),
    ]
