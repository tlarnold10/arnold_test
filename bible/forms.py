from django import forms
from .models import Emotion, Verse
from django.core.exceptions import ValidationError

class EmotionForm(forms.ModelForm):
	class Meta:
		model = Emotion
		fields = '__all__'
		# this could also be "fields = ['name', 'slug']"

class VerseForm(forms.ModelForm):
	class Meta: 
		model = Verse
		fields = '__all__'