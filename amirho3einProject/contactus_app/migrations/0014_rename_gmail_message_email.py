# Generated by Django 4.2.2 on 2023-07-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0013_rename_fname_message_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='gmail',
            new_name='email',
        ),
    ]
