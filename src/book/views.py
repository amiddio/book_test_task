from rest_framework import viewsets

from .models import Book
from .paginations import BookPagination
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Сэт-представление книг"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BookPagination

