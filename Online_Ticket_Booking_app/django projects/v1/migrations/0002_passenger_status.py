# Generated by Django 3.2.2 on 2021-07-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
