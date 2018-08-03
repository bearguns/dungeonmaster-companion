from django.contrib import admin

# Register your models here.
from .models import Campaign, Session, Player

admin.site.register(Campaign)
admin.site.register(Session)
admin.site.register(Player)
