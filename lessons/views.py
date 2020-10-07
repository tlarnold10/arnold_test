from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, DetailView
import pdb, psycopg2, re
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

# Time for everyone's favorite thing, reporting. 
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
		common = most_common_words(table)
		return render(request, 'lessons/lesson_report.html', context = {'testing':table.data, 'headers':table.columns, 'total':total, 'common_words':common})

# Generates the html for a stand alone report of my lessons learned. For learning purposes
def html_report(table):
	f = open('helloworld.html','w')
	webpage = """<html>\n<head></head>\n<body>\n<table style="border:1px solid black">\n<thead>\n"""
	for column in table.columns:
		webpage = webpage + """<th style="border:1px solid black">""" + column + "</th>\n"
	webpage = webpage + "</thead>\n"

	for row in table.data:
		webpage = webpage + """<tr>\n"""
		for dp in row:
			webpage = webpage + """<td style="border:1px solid black">""" + dp + "</td>\n"
		webpage = webpage + "</tr>"
	webpage = webpage + """</table>\n</body>\n</html>"""
	f.write(webpage)
	f.close()
	return table

# I want to get the word that most occures in my lesons, exluding commonly used words. 
def most_common_words(table):
	word_count = {}
	lessons = []
	bad_words = ['AND','THE', 'I', 'TO', 'A', 'IS', 'YOU', 'IN', 'OF', 'THAT', 
					'BE', 'ARE', 'YOUR', 'WITH', 'THINGS', 'ON', 'IT', '', 'FOR']
	for data in table.data:
		lessons.append(data[0])
	for lesson in lessons:
		for word in lesson.split():
			word = re.sub('[^a-zA-Z]', '', word).upper()
			if word in word_count and word not in bad_words:
				word_count[word] += 1
			elif word not in bad_words:
				word_count[word] = 1
	if word_count.keys() in bad_words:
		print(word_count.keys())
		for word in bad_words:
			del word_count[word]
	sorted_word_count = {}
	for k in sorted(word_count, key=word_count.get, reverse=True):
		sorted_word_count[k] = word_count[k]
	ranking = 0
	top_words = []
	for word in list(sorted_word_count):
		top_words.append(word)
		ranking += 1
		if ranking == 3:
			break
	return top_words