# Generated by Django 4.0.6 on 2022-07-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_user_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm',
            field=models.CharField(default='', max_length=50),
        ),
    ]