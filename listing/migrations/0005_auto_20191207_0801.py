# Generated by Django 3.0 on 2019-12-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_auto_20191207_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='email',
            field=models.EmailField(default='1236584125', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='phone',
            field=models.CharField(default='Loards@loards.com', max_length=100),
            preserve_default=False,
        ),
    ]