# Generated by Django 3.2 on 2021-05-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210508_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='game_round',
            field=models.IntegerField(default=1),
        ),
    ]