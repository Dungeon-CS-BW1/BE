# Generated by Django 3.0.2 on 2020-01-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0010_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='player',
            new_name='player_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='room',
            new_name='room_id',
        ),
    ]
