# Generated by Django 4.2.2 on 2023-06-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0003_info_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
    ]