from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
