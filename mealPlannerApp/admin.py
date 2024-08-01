from django.contrib import admin
from .models import Macros, Food

@admin.register(Macros)
class MacrosAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'protein', 'fat', 'carbs')
    search_fields = ('user__username', 'name')
    list_filter = ('user',)
    ordering = ('user', 'name')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'protein', 'fat', 'carbs')
    search_fields = ('user__username', 'name')
    list_filter = ('user',)
    ordering = ('user', 'name')