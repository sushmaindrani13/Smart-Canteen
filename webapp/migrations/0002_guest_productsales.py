# Generated by Django 2.2.3 on 2020-04-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='productsales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('yearmonth', models.CharField(max_length=100)),
                ('tamt', models.CharField(max_length=100)),
                ('prod', models.CharField(max_length=100)),
            ],
        ),
    ]