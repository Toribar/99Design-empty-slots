from django.contrib import admin

from .models import Contests

class ContestsAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']


admin.site.register(Contests, ContestsAdmin)

