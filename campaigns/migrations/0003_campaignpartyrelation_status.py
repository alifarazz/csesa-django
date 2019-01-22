# Generated by Django 2.0.9 on 2019-01-22 18:00

import campaigns.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20181230_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignpartyrelation',
            name='status',
            field=enumfields.fields.EnumField(default='approved', enum=campaigns.models.CampaignPartyRelationStatus, max_length=1000),
            preserve_default=False,
        ),
    ]
