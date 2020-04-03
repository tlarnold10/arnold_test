from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.generic import View

import pdb

from lessons.models import Book, Lesson
from bible.models import Verse, Emotion
from .serializers import BookSerializer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'javascript.html')

# Create your views here.
class JavaScript(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        book_count = Book.objects.all().count()
        lesson_count = Lesson.objects.all().count()
        verse_count = Verse.objects.all().count()
        emotion_count = Emotion.objects.all().count()
        header = ["Books", "Lessons", "Verses", "Emotion", "Test1", "Test2"]
        records = [book_count, lesson_count, verse_count, emotion_count, 12, 10]
        data = {
            "label": header,
            "default": records
        }
        return Response(data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer