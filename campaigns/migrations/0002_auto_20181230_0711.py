# Generated by Django 2.0.9 on 2018-12-30 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignpartyrelation',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cprelations', to='campaigns.Campaign'),
        ),
    ]
