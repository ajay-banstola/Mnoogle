# Generated by Django 2.1.7 on 2019-04-07 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobs_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='flag',
        ),
    ]
