import datetime
from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    campaign_notes = models.TextField(blank=True)
    completed = models.BooleanField(
        default=False,
        blank=True
    )
    completed_date = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Session(models.Model):
    start_date = models.DateTimeField()
    session_name = models.CharField(
        blank=False,
        max_length=200,
        default=f'{datetime.date.today()}'
    )
    session_notes = models.TextField()
    campaign = models.ForeignKey(
        Campaign,
        related_name='sessions',
        on_delete=models.CASCADE,
    )
    current_objective = models.CharField(
        blank=True,
        max_length=280,
    )

    def __str__(self):
        return self.session_name

class Player(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        related_name='players',
        on_delete=models.CASCADE,
    )

    # race options
    DRAGONBORN = 'Dragonborn'
    DWARF = 'Dwarf'
    ELF = 'Elf'
    GNOME = 'Gnome'
    HUMAN = 'Human'
    HALFLING = 'Halfling'
    HALF_ELF = 'Half-Elf'
    HALF_ORC = 'Half-Orc'
    TIEFLING = 'Tiefling'
    RACE_CHOICES = (
        (DRAGONBORN, DRAGONBORN),
        (DWARF, DWARF),
        (ELF, ELF),
        (GNOME, GNOME),
        (HUMAN, HUMAN),
        (HALFLING, HALFLING),
        (HALF_ELF, HALF_ELF),
        (HALF_ORC, HALF_ORC),
        (TIEFLING, TIEFLING)
    )

    # class choices
    BARBARIAN = 'Barbarian'
    BARD = 'Bard'
    CLERIC = 'Cleric'
    DRUID = 'Druid'
    FIGHTER = 'Fighter'
    MONK = 'Monk'
    PALADIN = 'Paladin'
    RANGER = 'Ranger'
    ROGUE = 'Rogue'
    SORCERER = 'Sorcerer'
    WARLOCK = 'Warlock'
    WIZARD = 'Wizard'
    CLASS_CHOICES = (
        (BARBARIAN, BARBARIAN),
        (BARD, BARD),
        (CLERIC, CLERIC),
        (DRUID, DRUID),
        (FIGHTER, FIGHTER),
        (MONK, MONK),
        (PALADIN, PALADIN),
        (RANGER, RANGER),
        (ROGUE, ROGUE),
        (SORCERER, SORCERER),
        (WARLOCK, WARLOCK),
        (WIZARD, WIZARD)
    )

    irl_name = models.CharField(
        blank=False,
        max_length=200
    )
    char_name = models.CharField(
        blank=False,
        max_length=200
    )
    char_race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default=HUMAN
    )
    char_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES,
        default=BARBARIAN
    )
    char_level = models.IntegerField(
        default=1
    )
    char_sheet = models.URLField(
        blank=True,
        max_length=100
    )
    inspiration = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return self.char_name

class Encounter(models.Model):
    name = models.CharField(max_length=200)
    trigger = models.TextField()
    rewards = models.TextField(blank=True)
    description = models.TextField()
    completed = models.BooleanField(blank=True)
    skipped = models.BooleanField(blank=True)
    session = models.ForeignKey(
        Session,
        related_name='encounters',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Monster(models.Model):
    name = models.CharField(max_length=64)
    hit_points = models.IntegerField()
    url = models.URLField()
    encounters = models.ForeignKey(
        Encounter,
        related_name='monsters',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
