# Generated by Django 2.1 on 2018-08-03 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_manager', '0007_auto_20180803_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irl_name', models.CharField(max_length=200)),
                ('char_name', models.CharField(max_length=200)),
                ('char_race', models.CharField(choices=[('Dragonborn', 'Dragonborn'), ('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Gnome', 'Gnome'), ('Human', 'Human'), ('Halfling', 'Halfling'), ('Half-Elf', 'Half-Elf'), ('Half-Orc', 'Half-Orc'), ('Tiefling', 'Tiefling')], default='Human', max_length=10)),
                ('char_class', models.CharField(choices=[('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Monk', 'Monk'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Rogue', 'Rogue'), ('Sorcerer', 'Sorcerer'), ('Warlock', 'Warlock'), ('Wizard', 'Wizard')], default='Barbarian', max_length=10)),
                ('char_level', models.IntegerField(default=1)),
                ('char_sheet', models.URLField(blank=True, max_length=100)),
                ('inspiration', models.BooleanField(blank=True, default=False)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='campaign_manager.Campaign')),
            ],
        ),
    ]
