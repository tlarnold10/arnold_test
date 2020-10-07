from django.db import models
from django.urls import reverse

BOOK_TOPICS = (
    ('leadership', 'leadership'),
    ('self improvement', 'self improvement'),
    ('technology', 'technology'),
    ('story', 'story'),
    ('fiction', 'fiction'),
    ('sales', 'sales'),
    ('management', 'management')
)

class Book(models.Model):
    book_name = models.CharField(max_length=50, unique=True)
    book_author = models.CharField(max_length=100)
    book_topic = models.CharField(max_length=50, choices=BOOK_TOPICS, default='leadership')
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.book_name
    
    class Meta:
        ordering = ['book_name']
    
    def get_absolute_url(self):
        return reverse('book_list')
    
    def get_new_url(self):
        return reverse('lesson_list', kwargs={'book': self.slug})

class Lesson(models.Model):
    lesson = models.TextField()
    slug = models.SlugField(max_length=25)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['lesson']

    def get_absolute_url(self):
    	return reverse('lesson_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
    	return reverse('lesson_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
    	return reverse('lesson_delete', kwargs={'slug': self.slug})