# Generated by Django 5.1.6 on 2025-02-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userdata_avatar_url_userdata_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='avatar_url',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='following',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='public_repos',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='updated_at',
        ),
    ]
