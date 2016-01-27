from django.contrib import admin

from .models import Contest

class ContestAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date']


admin.site.register(Contest, ContestAdmin)

