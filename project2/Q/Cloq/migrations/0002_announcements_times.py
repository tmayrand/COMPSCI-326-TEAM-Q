# Generated by Django 2.0.2 on 2018-03-20 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cloq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('aid', models.AutoField(help_text='Announcement identifier.', primary_key=True, serialize=False)),
                ('text', models.TextField(help_text='Announcement body.')),
                ('time', models.DateTimeField(default=datetime.datetime.now, help_text='Announcement datetime.')),
                ('usertype', models.IntegerField(help_text='Allowed user types (1 = user, 2 = admin + user).')),
                ('title', models.CharField(help_text='Announcement title.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='times',
            fields=[
                ('tid', models.AutoField(help_text='Timestamp identifier.', primary_key=True, serialize=False)),
                ('timetype', models.IntegerField(help_text='Time type (1 = punch in, 2 = punch out, 3 = schedule, 4 = unavailable)')),
                ('start', models.DateTimeField(default=datetime.datetime.now, help_text='Start datetime.')),
                ('end', models.DateTimeField(default=datetime.datetime.now, help_text='End datetime.')),
                ('uid', models.IntegerField(help_text='Associated user ID.')),
            ],
        ),
    ]
