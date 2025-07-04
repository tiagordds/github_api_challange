# Generated by Django 5.1.6 on 2025-04-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=150, unique=True)),
                ('avatar_url', models.URLField()),
                ('html_url', models.URLField()),
                ('followers_url', models.URLField()),
                ('following_url', models.URLField()),
                ('gist_url', models.URLField()),
                ('starred_url', models.URLField()),
                ('subscriptions_url', models.URLField()),
                ('organizations_url', models.URLField()),
                ('repos_url', models.URLField()),
                ('event_url', models.URLField()),
                ('received_events_url', models.URLField()),
                ('user_type', models.CharField(max_length=200)),
                ('user_view_type', models.CharField(max_length=200)),
                ('site_admin', models.BooleanField()),
            ],
        ),
    ]
