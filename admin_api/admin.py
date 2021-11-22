from django.contrib import admin
from .models import Advisor
# Register your models here.

class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['advisor_name', 'photo_url']
admin.site.register(Advisor, AdvisorAdmin)