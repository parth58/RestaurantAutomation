# Generated by Django 2.2 on 2019-04-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0004_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentorder',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
