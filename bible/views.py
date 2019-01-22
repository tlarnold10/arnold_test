from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, DetailView

from .models import Emotion, Verse
from .forms import EmotionForm, VerseForm

# Create your views here.
class EmotionList(View):
	template_name = 'bible/emotion_list.html'

	def get(self, request):
		emotions = Emotion.objects.all()
		context = {'emotion_list':emotions}
		return render(request, self.template_name, context)

class EmotionCreate(CreateView):
	form_class = EmotionForm
	template_name = 'bible/emotion_create.html'

class VerseList(DetailView):
	template_name = 'bible/verse_list.html'
	emotion = ''

	def get(self, request, emotion):
		Verse.objects.values_list('emotion', flat=True)
		verses = Verse.objects.filter(emotion__slug=emotion)
		context = {'verse_list':verses}
		return render(request, self.template_name, context)

class VerseCreate(CreateView):
	form_class = VerseForm
	template_name = 'bible/verse_create.html'

class VerseDetail(DetailView):
	model = Verse