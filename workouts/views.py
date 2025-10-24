from django.shortcuts import render, redirect
from .models import Workout, Exercise

# Create your views here.
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    
    context = {'workouts': workouts}
    return render(request, 'workouts/workout_list.html', context)

def add_workout(request):
    if request.method == 'POST':
        workout_date =request.POST.get('date')
        
        new_workout = Workout.objects.create(date=workout_date)
        
        exercise_name = request.POST.get('exercise_name')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        
        Exercise.objects.create(
            workout=new_workout,
            name=exercise_name,
            sets=sets,
            reps=reps
        )
        
        return redirect('workout_list')
    return render(request, 'workouts/add_workout.html')