from django.contrib import admin
from .models import NutritionLog, FoodEntry, MealSuggestion

class FoodEntryInline(admin.TabularInline):
    model = FoodEntry
    extra = 1

@admin.register(NutritionLog)
class NutritionLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'user']
    list_filter = ['date', 'user']
    inlines = [FoodEntryInline]

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'carbohydrates', 'fats', 'nutrition_log']
    list_filter = ['nutrition_log__date']
    search_fields = ['name', 'barcode']

@admin.register(MealSuggestion)
class MealSuggestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_type', 'calories', 'is_active']
    list_filter = ['meal_type', 'is_active']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'meal_type', 'is_active')
        }),
        ('Macronutrients', {
            'fields': ('calories', 'protein', 'carbohydrates', 'fats')
        }),
        ('Micronutrient Highlights', {
            'fields': ('high_in_vitamin_d', 'high_in_vitamin_b12', 'high_in_iron', 
                      'high_in_calcium', 'high_in_omega3')
        }),
    )
