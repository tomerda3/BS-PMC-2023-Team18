# Generated by Django 3.2.9 on 2022-01-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_userprofileinfo_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='aboutme',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
