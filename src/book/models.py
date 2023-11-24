from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    """Модель книг"""

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = ISBNField(clean_isbn=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.author}"
