# Generated by Django 4.2.5 on 2023-09-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='No title', max_length=256),
        ),
    ]
