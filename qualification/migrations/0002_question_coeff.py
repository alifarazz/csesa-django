# Generated by Django 2.0.9 on 2018-12-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='coeff',
            field=models.IntegerField(default=1),
        ),
    ]
