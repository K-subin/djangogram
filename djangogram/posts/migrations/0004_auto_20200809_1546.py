# Generated by Django 3.0.8 on 2020-08-09 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200809_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
    ]