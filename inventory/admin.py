from django.contrib import admin
from .models import Device, Returned_laptop, Lended


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('laptop_name', 'make', 'serial_number', 'color', 'condition', 'updated_at')
    # list_filter = ('laptop_name', 'lendee', 'make', 'serial_number', 'lended_at')
    # search_fields = ('laptop_name', 'lendee', 'make', 'serial_number', 'lended_at', 'city')


@admin.register(Returned_laptop)
class Returned_laptopAdmin(admin.ModelAdmin):
    list_display = ('returned_name', 'lended_person', 'make', 'serial_number', 'returned_at')
    list_filter = ('returned_name', 'lended_person', 'make', 'serial_number', 'returned_at')
   

@admin.register(Lended)
class LendedAdmin(admin.ModelAdmin):
    list_display = ('lended_laptop_name', 'lendee', 'serial_number','lending_condition', 'lended_at')
    list_filter = ('lended_laptop_name', 'lendee',  'serial_number', 'lended_at')
    

