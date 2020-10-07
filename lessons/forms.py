from django import forms
from .models import Book, Lesson
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'
		# this could also be "fields = ['name', 'slug']"

class LessonForm(forms.ModelForm):
	class Meta: 
		model = Lesson
		fields = '__all__'