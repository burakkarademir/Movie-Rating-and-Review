# Generated by Django 3.0.6 on 2020-06-04 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_soundtrack',
            old_name='sountrack_id',
            new_name='soundtrack_id',
        ),
    ]
