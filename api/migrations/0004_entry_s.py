# Generated by Django 3.2 on 2021-05-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_entry_avg_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='s',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]