from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import FoodEntryForm
from .models import NutritionLog, FoodEntry, MealSuggestion

@login_required
def nutrition_log_list(request):
    """Display list of nutrition logs for the current user"""
    nutrition_logs = NutritionLog.objects.filter(user=request.user).prefetch_related('food_entries')
    context = {'nutrition_logs': nutrition_logs}
    return render(request, 'nutrition/nutrition_log_list.html', context)

@login_required
def add_nutrition_log(request):
    """Add a new nutrition log with food entries"""
    FoodEntryFormSet = inlineformset_factory(
        NutritionLog, FoodEntry, form=FoodEntryForm, extra=1, can_delete=True
    )
    
    if request.method == 'POST':
        log_date = request.POST.get('date')
        
        if log_date:
            nutrition_log = NutritionLog(date=log_date, user=request.user)
            formset = FoodEntryFormSet(request.POST, instance=nutrition_log)
            
            if formset.is_valid():
                nutrition_log.save()
                formset.save()
                return redirect('nutrition_log_list')
    else:
        formset = FoodEntryFormSet()
    
    return render(request, 'nutrition/add_nutrition_log.html', {'formset': formset})

@login_required
def barcode_scanner(request):
    """Placeholder view for barcode scanning functionality"""
    # This is a placeholder for future integration with barcode scanning APIs
    # Popular food databases: Open Food Facts, USDA FoodData Central
    context = {
        'message': 'Barcode scanning feature - Ready for integration with Open Food Facts API',
        'supported_databases': [
            'Open Food Facts (openfoodfacts.org)',
            'USDA FoodData Central',
            'Nutritionix API'
        ]
    }
    return render(request, 'nutrition/barcode_scanner.html', context)

@login_required
def meal_suggestions(request):
    """Display meal suggestions based on nutritional gaps"""
    # Get user's nutrition data for the current day
    from datetime import date
    today_logs = NutritionLog.objects.filter(user=request.user, date=date.today())
    
    # Calculate total nutrients consumed today
    totals = FoodEntry.objects.filter(nutrition_log__in=today_logs).aggregate(
        total_vitamin_d=Sum('vitamin_d'),
        total_vitamin_b12=Sum('vitamin_b12'),
        total_iron=Sum('iron'),
        total_calcium=Sum('calcium'),
        total_omega3=Sum('omega3'),
    )
    
    # Determine nutritional gaps (simplified logic)
    # Recommended daily values (simplified)
    rdv = {
        'vitamin_d': 20,  # mcg
        'vitamin_b12': 2.4,  # mcg
        'iron': 18,  # mg
        'calcium': 1000,  # mg
        'omega3': 1.6,  # g
    }
    
    gaps = {}
    for nutrient, recommended in rdv.items():
        consumed = totals.get(f'total_{nutrient}') or 0
        if consumed < recommended * 0.7:  # Less than 70% of RDV
            gaps[nutrient] = True
    
    # Get meal suggestions that fill these gaps
    suggestions = MealSuggestion.objects.filter(is_active=True)
    
    # Filter suggestions based on gaps
    if gaps.get('vitamin_d'):
        suggestions = suggestions.filter(high_in_vitamin_d=True)
    if gaps.get('vitamin_b12'):
        suggestions = suggestions.filter(high_in_vitamin_b12=True)
    if gaps.get('iron'):
        suggestions = suggestions.filter(high_in_iron=True)
    if gaps.get('calcium'):
        suggestions = suggestions.filter(high_in_calcium=True)
    if gaps.get('omega3'):
        suggestions = suggestions.filter(high_in_omega3=True)
    
    # If no specific gaps, show all suggestions
    if not gaps:
        suggestions = MealSuggestion.objects.filter(is_active=True)[:10]
    
    context = {
        'suggestions': suggestions,
        'gaps': gaps,
        'totals': totals,
        'rdv': rdv,
    }
    return render(request, 'nutrition/meal_suggestions.html', context)
