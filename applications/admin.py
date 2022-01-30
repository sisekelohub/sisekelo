from django.contrib import admin
from .models import  Application, Qualification


# admin.site.register(Qualification)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'surname', 'equity', 'phone_number', 'qualification', 'email', 'next_of_keen_name', 'next_of_keen_cellphone')
    # list_filter = ('course', 'equity', 'qualification ', 'email')
    search_fields = ('course', 'equity', 'qualification', 'email', 'name')


# @admin.register(Qualification)
# class Highest_qualificationAdmin(admin.ModelAdmin):
#     list_display = ('qualification_number', 'qualification')
#     list_filter = ('qualification_number', 'qualification')
#     search_fields = ('qualification_number', 'qualification')