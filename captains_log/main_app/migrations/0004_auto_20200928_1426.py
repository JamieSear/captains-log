# Generated by Django 3.1.1 on 2020-09-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_matchreport_captain_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captains',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
