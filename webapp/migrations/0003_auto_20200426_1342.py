# Generated by Django 3.0.5 on 2020-04-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_guest_productsales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tot',
            field=models.IntegerField(),
        ),
    ]
