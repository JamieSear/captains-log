# Generated by Django 3.1.1 on 2020-10-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_delete_teamplayers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchreport',
            name='message',
            field=models.CharField(max_length=10000),
        ),
    ]
