# Generated by Django 4.2.2 on 2023-07-01 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0012_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='fname',
            new_name='name',
        ),
    ]
