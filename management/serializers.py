from rest_framework import serializers

from lessons.models import Book, Lesson

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['book_name', 'book_author']