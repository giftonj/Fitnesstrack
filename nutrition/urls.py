from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition_log_list, name='nutrition_log_list'),
    path('add/', views.add_nutrition_log, name='add_nutrition_log'),
    path('barcode-scanner/', views.barcode_scanner, name='barcode_scanner'),
    path('meal-suggestions/', views.meal_suggestions, name='meal_suggestions'),
]
