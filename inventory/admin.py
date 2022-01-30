from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('laptop_name', 'lendee', 'make', 'serial_number', 'lended_at', 'serial_number')
    list_filter = ('laptop_name', 'lendee', 'make', 'serial_number', 'lended_at')
    search_fields = ('laptop_name', 'lendee', 'make', 'serial_number', 'lended_at', 'city')
