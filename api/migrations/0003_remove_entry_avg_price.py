# Generated by Django 3.2 on 2021-05-03 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_entry_z'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='avg_price',
        ),
    ]
