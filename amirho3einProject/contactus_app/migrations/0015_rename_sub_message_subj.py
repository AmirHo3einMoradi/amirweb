# Generated by Django 4.2.2 on 2023-07-01 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0014_rename_gmail_message_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sub',
            new_name='subj',
        ),
    ]