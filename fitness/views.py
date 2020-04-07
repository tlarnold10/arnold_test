from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, DetailView
from rest_framework import viewsets

from .models import Weight, PersonalBest, Workout
from .forms import WeightForm, PersonalBestForm, WorkoutForm
from .serializers import WeightSerializer

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

class WeightDelete(View):
    def get(self, request, weight_date):
        weight = Weight.objects.filter(weight_date=weight_date)
        weight.delete()
        return render(request, 'fitness/weight_delete.html', {'weight_date':weight_date})


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

class WeightChart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fitness/weight_chart.html')