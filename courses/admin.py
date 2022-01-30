from django.contrib import admin
from .models import Learnership,  Short_Course, Nfq, Accredited_Program, Specialized_Course, Program_Catalogue

admin.site.register(Program_Catalogue)


@admin.register(Specialized_Course)
class Specialized_CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'mode_of_delivery', 'duration', 'status', 'image')
    list_filter = ('status', 'duration')
    search_fields = ('title', 'duration')


@admin.register(Accredited_Program)
class Accredited_ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'certificate_type', 'mode_of_delivery', 'nfq_level', 'duration', 'is_published')
    list_filter = ('status', 'nfq_level', 'duration')
    search_fields = ('title', 'nfq_level', 'duration')


@admin.register(Nfq)
class NfqAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('name', 'level')
    search_fields = ('name', 'level')

# @admin.register(Skills_Program)
# class Skills_ProgramAdmin(admin.ModelAdmin):
#     list_display = ('title', 'mode_of_delivery', 'duration', 'status', 'image')
#     list_filter = ('status',  'duration')
#     search_fields = ('title',  'duration')

@admin.register(Learnership)
class LearnershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'certificate_type', 'mode_of_delivery', 'duration', 'price', 'start_date')
    list_filter = ('status', 'nfq_level', 'duration')
    search_fields = ('title', 'nfq_level', 'duration')
    list_editable = ('start_date', 'duration', 'price', 'mode_of_delivery')

@admin.register(Short_Course)
class Short_CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'mode_of_delivery', 'duration')
    list_filter = ('price',  'duration')
    search_fields = ('title',  'duration')

# @admin.register(Program_Catalogues)
# class Program_CataloguesAdmin(admin.ModelAdmin):
#     list_display = ('name')
#     list_filter = ('name')
#     search_fields = ('name')