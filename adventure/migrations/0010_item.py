# Generated by Django 3.0.2 on 2020-01-09 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0009_auto_20200109_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default item', max_length=100)),
                ('staminaPoints', models.IntegerField(default=5)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
    ]
