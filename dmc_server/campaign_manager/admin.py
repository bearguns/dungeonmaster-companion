from django.contrib import admin

# Register your models here.
from .models import Campaign, Session, Player, Encounter, Monster

class SessionInline(admin.StackedInline):
    model = Session

class CampaignAdmin(admin.ModelAdmin):
    inlines = [
        SessionInline,
    ]

class EncounterInline(admin.StackedInline):
    model = Encounter

class SessionAdmin(admin.ModelAdmin):
    inlines = [
        EncounterInline
    ]

class CreatureInline(admin.StackedInline):
    model = Monster

class EncounterAdmin(admin.ModelAdmin):
    inlines = [
        CreatureInline,
    ]
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Player)
admin.site.register(Encounter, EncounterAdmin)
