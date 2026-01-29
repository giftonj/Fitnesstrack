from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from .forms import ExerciseForm
from .models import Workout, Exercise

# Create your views here.
@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    
    
    context = {'workouts': workouts}
    return render(request, 'workouts/workout_list.html', context)

@login_required
def add_workout(request):
    ExerciseFormSet =inlineformset_factory(Workout, Exercise, form=ExerciseForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        
        #Get the workout date from the submited work
        workout_date = request.POST.get('date')
        
        
        #create a new unsaved workout instance
        workout = Workout(date=request.POST.get('date'), user=request.user)
        
        #create a formset instance with the submited data and linking it to the new workout
        formset = ExerciseFormSet(request.POST, instance=workout)
        
       
        if formset.is_valid() and workout_date:
            workout.save()
            formset.save()
        
            return redirect('workout_list')
        
    else:
            formset = ExerciseFormSet()
            
    return render(request, 'workouts/add_workout.html', {'formset': formset})