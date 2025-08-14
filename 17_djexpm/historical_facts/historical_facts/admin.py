from django.contrib import admin
from .models import Category, HistoricalFact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(HistoricalFact)
class HistoricalFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'
    list_editable = ('is_featured',)