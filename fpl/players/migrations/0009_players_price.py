# Generated by Django 4.0.1 on 2022-02-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_players_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
