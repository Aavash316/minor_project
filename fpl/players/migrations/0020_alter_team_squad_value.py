# Generated by Django 4.0.1 on 2022-03-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_alter_team_squad_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='squad_value',
            field=models.IntegerField(default=0),
        ),
    ]
