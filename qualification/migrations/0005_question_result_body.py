# Generated by Django 2.0.9 on 2019-01-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0004_auto_20190102_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='result_body',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
