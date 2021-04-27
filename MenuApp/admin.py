from django.contrib import admin
from .models import Category
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display: tuple = 'parent', 'title'
    list_display_links: tuple = 'parent', 'title'
    sortable_by = 'parent'
