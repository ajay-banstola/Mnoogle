# Generated by Django 2.1.7 on 2019-04-09 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190409_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='Job_Id',
        ),
    ]
