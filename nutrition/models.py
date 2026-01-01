from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class NutritionLog(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.date.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-date']

class FoodEntry(models.Model):
    nutrition_log = models.ForeignKey(NutritionLog, on_delete=models.CASCADE, related_name='food_entries')
    name = models.CharField(max_length=200)
    
    # Macronutrients
    calories = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Grams")
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Grams")
    fats = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Grams")
    
    # Micronutrients (most important ones)
    vitamin_d = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Micrograms (mcg)")
    vitamin_b12 = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Micrograms (mcg)")
    iron = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Milligrams (mg)")
    calcium = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Milligrams (mg)")
    omega3 = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Grams")
    
    # Barcode for product identification
    barcode = models.CharField(max_length=50, blank=True, null=True, help_text="Product barcode (UPC/EAN)")
    
    # Serving information
    serving_size = models.CharField(max_length=100, blank=True, help_text="e.g., '1 cup', '100g'")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.calories} cal"
    
    class Meta:
        ordering = ['-created_at']

class MealSuggestion(models.Model):
    """Pre-defined meal suggestions based on nutritional profile"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    # Nutritional profile
    calories = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Key micronutrients this meal is rich in
    high_in_vitamin_d = models.BooleanField(default=False)
    high_in_vitamin_b12 = models.BooleanField(default=False)
    high_in_iron = models.BooleanField(default=False)
    high_in_calcium = models.BooleanField(default=False)
    high_in_omega3 = models.BooleanField(default=False)
    
    # Categorization
    meal_type = models.CharField(max_length=50, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ])
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['meal_type', 'name']
