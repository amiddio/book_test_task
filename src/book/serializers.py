from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Сериалайзер книг"""

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'publication_date', 'isbn')
