# Generated by Django 4.0.1 on 2022-02-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0011_team_transfer_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='transfer_counter',
            field=models.IntegerField(default=1),
        ),
    ]