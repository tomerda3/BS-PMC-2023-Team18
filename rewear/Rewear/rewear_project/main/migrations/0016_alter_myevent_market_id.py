# Generated by Django 3.2.18 on 2023-05-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_myevent_market_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='market_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
