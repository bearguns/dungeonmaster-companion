from django.contrib import admin

# Register your models here.
from .models import Campaign
from .models import Session

admin.site.register(Campaign)
admin.site.register(Session)
