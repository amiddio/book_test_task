from rest_framework import routers

from .views import BookViewSet

router = routers.SimpleRouter()

# Router list
router.register(r'books', BookViewSet)
