# Generated by Django 2.2.7 on 2019-12-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
