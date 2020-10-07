from django import forms
from .models import Workout, Weight, PersonalBest
from django.core.exceptions import ValidationError

class WorkoutForm(forms.ModelForm):
	class Meta:
		model = Workout
		fields = ['workout_duration', 'workout_type']

class WeightForm(forms.ModelForm):
	class Meta: 
		model = Weight
		fields = ['weight_weight']

class PersonalBestForm(forms.ModelForm):
	class Meta: 
		model = PersonalBest
		fields = ['pr_lift', 'pr_weight', 'pr_reps']
