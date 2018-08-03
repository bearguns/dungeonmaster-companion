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
