from django.contrib import admin
from .models import Faq_Categorie, Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')
    list_filter = ('category', 'title')
    search_fields = ('title', 'category')
    # prepopulated_fields = {'slug': ('title',)}
    # #raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')

@admin.register(Faq_Categorie)
class Faq_categorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_filter = ('name')
    # search_fields = ('name')
