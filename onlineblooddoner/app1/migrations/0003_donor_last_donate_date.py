# Generated by Django 2.2.4 on 2019-11-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='last_donate_date',
            field=models.DateField(default=False),
        ),
    ]
