# Generated by Django 4.0.5 on 2022-06-06 12:31

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=1000)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
            ],
            options={
                'verbose_name_plural': 'memories',
            },
        ),
    ]