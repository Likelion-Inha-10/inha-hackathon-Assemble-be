# Generated by Django 4.0.6 on 2022-07-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_notice_group_body_group_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newfile',
            name='myfile',
            field=models.TextField(),
        ),
    ]