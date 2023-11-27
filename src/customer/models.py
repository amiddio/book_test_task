from django.db import models


class Customer(models.Model):
    """Модель пользователя"""

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
