# Generated by Django 5.0.6 on 2024-06-01 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findstaff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='house_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findstaff.house'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findstaff.room'),
        ),
    ]