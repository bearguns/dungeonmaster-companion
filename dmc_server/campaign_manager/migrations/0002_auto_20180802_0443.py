# Generated by Django 2.1 on 2018-08-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='current_objective',
            field=models.CharField(blank=True, max_length=280),
        ),
    ]
