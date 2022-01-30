from django.contrib import admin

from .models import  Contact


# admin.site.register(Qualification)


@admin.register(Contact)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cell', 'message')
    # list_filter = ('course', 'equity', 'qualification ', 'email')
    search_fields = ('email', 'cell')