from django.db import models
from django.urls import reverse

WORKOUT_TYPES = (
                ('run','run'),
                ('bike','bike'),
                ('lift','lift'),
                ('beach body lift','beach body lift'),
                ('beach body cardio','beach body cardio'),
                ('beach body boxing','beach body boxing'),
                ('lift from home','lift from home'),
                ('crossfit / HIT','crossfit / HIT'),
)

class Workout(models.Model):
    workout_date = models.DateField(auto_now_add=True)
    workout_duration = models.IntegerField()
    workout_type = models.CharField(choices=WORKOUT_TYPES, default='lift from home', max_length=100)

    class Meta:
        ordering = ['workout_date']

    def get_absolute_url(self):
        return reverse('workout_list')

    def get_delete_url(self):
    	return reverse('workout_delete', kwargs={'workout_date': self.workout_date})


class PersonalBest(models.Model):
    pr_date = models.DateField(auto_now_add=True)
    pr_lift = models.CharField(max_length=50)
    pr_weight = models.IntegerField()
    pr_reps = models.IntegerField()


class Weight(models.Model):
    weight_date = models.DateField(auto_now_add=True)
    weight_weight = models.IntegerField()

    class Meta:
        ordering = ['weight_date']

    def get_absolute_url(self):
        return reverse('weight_list')

    def get_delete_url(self):
    	return reverse('weight_delete', kwargs={'weight_date': self.weight_date})