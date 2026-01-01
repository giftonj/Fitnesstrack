from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from .models import NutritionLog, FoodEntry, MealSuggestion

class NutritionLogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_nutrition_log_creation(self):
        """Test creating a nutrition log"""
        log = NutritionLog.objects.create(user=self.user, date=date.today())
        self.assertEqual(str(log), f"testuser - {date.today().strftime('%Y-%m-%d')}")
        
    def test_food_entry_creation(self):
        """Test creating a food entry with micronutrients"""
        log = NutritionLog.objects.create(user=self.user, date=date.today())
        entry = FoodEntry.objects.create(
            nutrition_log=log,
            name="Salmon",
            calories=200,
            protein=25,
            carbohydrates=0,
            fats=12,
            vitamin_d=5.5,
            vitamin_b12=2.8,
            iron=0.5,
            calcium=15,
            omega3=2.5,
            barcode="123456789",
            serving_size="100g"
        )
        self.assertEqual(entry.name, "Salmon")
        self.assertEqual(entry.barcode, "123456789")
        self.assertEqual(float(entry.omega3), 2.5)
        
class NutritionViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
    def test_nutrition_log_list_view(self):
        """Test nutrition log list view"""
        response = self.client.get(reverse('nutrition_log_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutrition/nutrition_log_list.html')
        
    def test_add_nutrition_log_view(self):
        """Test add nutrition log view"""
        response = self.client.get(reverse('add_nutrition_log'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutrition/add_nutrition_log.html')
        
    def test_barcode_scanner_view(self):
        """Test barcode scanner view"""
        response = self.client.get(reverse('barcode_scanner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutrition/barcode_scanner.html')
        self.assertIn('supported_databases', response.context)
        
    def test_meal_suggestions_view(self):
        """Test meal suggestions view"""
        response = self.client.get(reverse('meal_suggestions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutrition/meal_suggestions.html')
        
    def test_login_required(self):
        """Test that views require login"""
        self.client.logout()
        response = self.client.get(reverse('nutrition_log_list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        
class MealSuggestionModelTest(TestCase):
    def test_meal_suggestion_creation(self):
        """Test creating a meal suggestion"""
        suggestion = MealSuggestion.objects.create(
            name="Grilled Salmon with Spinach",
            description="Rich in Omega-3 and Iron",
            calories=350,
            protein=30,
            carbohydrates=10,
            fats=20,
            high_in_omega3=True,
            high_in_iron=True,
            meal_type='lunch'
        )
        self.assertEqual(suggestion.name, "Grilled Salmon with Spinach")
        self.assertTrue(suggestion.high_in_omega3)
        self.assertTrue(suggestion.is_active)
        
    def test_meal_suggestion_filtering(self):
        """Test meal suggestions are filtered correctly"""
        # Clear any existing suggestions from data migration
        MealSuggestion.objects.all().delete()
        
        MealSuggestion.objects.create(
            name="Vitamin D Fortified Milk",
            description="Rich in Vitamin D and Calcium",
            calories=150,
            protein=8,
            carbohydrates=12,
            fats=8,
            high_in_vitamin_d=True,
            high_in_calcium=True,
            meal_type='breakfast'
        )
        
        suggestions = MealSuggestion.objects.filter(high_in_vitamin_d=True)
        self.assertEqual(suggestions.count(), 1)
