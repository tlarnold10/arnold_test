from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, DetailView
import pdb

from .models import Book, Lesson
from .forms import BookForm, LessonForm

# Create your views here.
class BookList(View):
	template_name = 'lessons/book_list.html'

	def get(self, request):
		books = Book.objects.all()
		context = {'book_list':books}
		return render(request, self.template_name, context)

class BookCreate(CreateView):
	form_class = BookForm
	template_name = 'lessons/book_create.html'

class LessonList(DetailView):
	template_name = 'lessons/lesson_list.html'
	book = ''

	def get(self, request, book):
		Lesson.objects.values_list('book', flat=True)
		lessons = Lesson.objects.filter(book__slug=book)
		context = {'lesson_list':lessons}
		return render(request, self.template_name, context)

class LessonCreate(CreateView):
	form_class = LessonForm
	template_name = 'lessons/lesson_create.html'

class LessonDetail(DetailView):
	model = Lesson

class LessonUpdate(View):
	form_class = LessonForm
	model = Lesson
	template_name = 'lessons/lesson_update.html'

	def get(self, request, slug):
		lesson = get_object_or_404(self.model, slug=slug)
		context = {
			'form':self.form_class(instance=lesson),
			'lesson':lesson,}
		return render(request, self.template_name, context)

	def post(self, request, slug):
		lesson = get_object_or_404(self.model, slug=slug)
		print(lesson.slug)
		bound_form = self.form_class(request.POST, instance=lesson)
		# if bound_form.is_valid():
		new_lesson = bound_form.save()
		return redirect(new_lesson)
#		else:
#			context = {
#				'form':bound_form,
#				'verse':verse,
#			}
#			return render(request, self.template_name, context)

class LessonDelete(View):
	def get(self, request, slug):
		lesson = get_object_or_404(Lesson, slug=slug)
		lesson.delete()
		return render(request, 'lessons/lesson_confirm_delete.html', {'lesson':lesson})

# 	def post(self, request, slug):
# 		verse = get_object_or_404(Verse, slug=slug)
# 		verse.delete()
# 		return redirect('bible/emotion_list.html')