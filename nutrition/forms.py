from django import forms
from .models import FoodEntry

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['name', 'calories', 'protein', 'carbohydrates', 'fats', 
                  'vitamin_d', 'vitamin_b12', 'iron', 'calcium', 'omega3',
                  'barcode', 'serving_size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'carbohydrates': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fats': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'vitamin_d': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'vitamin_b12': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'iron': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'calcium': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'omega3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Scan or enter barcode'}),
            'serving_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1 cup, 100g'}),
        }
