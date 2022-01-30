from django.contrib import admin
from .models import Event

#admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'mode', 'address', 'description', 'date')
    list_filter = ('status', 'created')
    search_fields = ('title', 'mode')
    #date_hierarchy = 'publish'
    #ordering = ('status')
