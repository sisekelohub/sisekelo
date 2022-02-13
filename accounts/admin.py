from django.contrib import admin


from .models import Profile

# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id',  'birth_date', 'city')
    list_filter = ('user',  'birth_date', 'city')
    search_fields = ('user', 'student_id',  'birthday', 'city')
