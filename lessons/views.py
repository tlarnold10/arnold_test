from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, DetailView
import pdb, psycopg2
import pandas as pa

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

class LessonReport(View):
	def get(self, request):
		table = pa.DataFrame(columns=['Lesson', 'Book Name', 'Book Topic'])
		conn = psycopg2.connect(host="localhost",database="arnold",user="postgres",password="snowlep")
		curs = conn.cursor()
		query = """
SELECT 
	l.lesson,
	b.book_name,
	b.book_topic
FROM lessons_lesson l
INNER JOIN lessons_book b
	ON l.book_id = b.id
ORDER BY book_name, lesson
	"""
		curs.execute(query)
		table.data = curs.fetchall()
		total = len(table.data)
		html_report(table)
		return render(request, 'lessons/lesson_report.html', context = {'testing':table.data, 'headers':table.columns, 'total':total})

def html_report(table):
	f = open('helloworld.html','w')
	webpage = """<html><head></head><body><table style="border:1px solid black"><thead>"""
	for column in table.columns:
		webpage = webpage + """<th style="border:1px solid black>""" + column + "</th>"
	webpage = webpage + "</thead>"
	
	for row in table.data:
		webpage = webpage + """<tr>"""
		for dp in row:
			webpage = webpage + """<td style="border:1px solid black>""" + dp + "</td>"
		webpage = webpage + "</tr>"
	webpage = webpage + """</table></body></html>"""
	f.write(webpage)
	f.close()
	return table