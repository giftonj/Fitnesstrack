from django.db import models
from django.utils import timezone

class Workout(models.Model):
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d Workout')
    
class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveBigIntegerField()
    reps = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.name} ({self.sets}x{self.reps})"