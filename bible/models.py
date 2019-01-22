from django.db import models
from django.urls import reverse

class Emotion(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(
		max_length=50,
		unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('emotion_list')

	def get_new_url(self):
		return reverse('verse_list', kwargs={'emotion': self.slug})

class Verse(models.Model):
	book = models.CharField(max_length=25)
	chapter = models.IntegerField()
	verses = models.CharField(max_length=10)
	text = models.TextField()
	slug = models.SlugField(max_length=25)
	emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

	class Meta:
		ordering = ['book']

	def get_absolute_url(self):
		return reverse('verse_detail', kwargs={'slug': self.slug})