from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomerSerializer


class CustomerAPIView(APIView):
    """Представление для создания пользователей"""

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response({'result': True}, status=status.HTTP_201_CREATED)

