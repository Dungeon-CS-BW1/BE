# Generated by Django 3.0.2 on 2020-01-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0011_auto_20200109_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='player_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='room_id',
            field=models.IntegerField(default=0),
        ),
    ]
