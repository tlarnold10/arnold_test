from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, DetailView
import pdb, psycopg2, re
import pandas as pa

from .models import Weight, PersonalBest, Workout
from .forms import WeightForm, PersonalBestForm, WorkoutForm

# Create your views here.
class WeightList(View):
	template_name = 'fitness/weight_list.html'

	def get(self, request):
		weights = Weight.objects.all()
		context = {'weight_list':weights}
		return render(request, self.template_name, context)

class WeightCreate(CreateView):
	form_class = WeightForm
	template_name = 'fitness/weight_create.html'