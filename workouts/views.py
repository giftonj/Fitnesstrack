from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from .forms import ExerciseForm
from .models import Workout, Exercise

# Create your views here.
@login_required #It automatically checks if a user is logged in before they can access a view. If they aren't, it redirects them to the login page.
def workout_list(request):
    #workouts = Workout.objects.all().order_by('-date')
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    
    
    context = {'workouts': workouts}
    return render(request, 'workouts/workout_list.html', context)

@login_required
def add_workout(request):
    ExerciseFormSet =inlineformset_factory(Workout, Exercise, form=ExerciseForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        #workout_date =request.POST.get('date')
        
        #Get the workout date from the submited work
        workout_date = request.POST.get('date')
        
        
        #create a new unsaved workout instance
        #workout = Workout(date=workout_date)
        workout = Workout(date=request.POST.get('date'), user=request.user)
        
        #create a formset instance with the submited data and linking it to the new workout
        formset = ExerciseFormSet(request.POST, instance=workout)
        
        #new_workout = Workout.objects.create(date=workout_date)
        
        #exercise_name = request.POST.get('exercise_name')
        #sets = request.POST.get('sets')
        #reps = request.POST.get('reps')
        
        #Exercise.objects.create(
            #workout=new_workout,
            #name=exercise_name,
            #sets=sets,
            #reps=reps
        #)
        if formset.is_valid() and workout_date:
            workout.save()
            formset.save()
        
            return redirect('workout_list')
        
    else:
            formset = ExerciseFormSet()
            
    return render(request, 'workouts/add_workout.html', {'formset': formset})