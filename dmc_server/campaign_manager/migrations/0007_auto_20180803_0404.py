# Generated by Django 2.1 on 2018-08-03 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_manager', '0006_auto_20180803_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='campaign_manager.Campaign'),
        ),
    ]
