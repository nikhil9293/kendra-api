# Generated by Django 3.2.5 on 2021-09-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand_elexon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='Demand',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
