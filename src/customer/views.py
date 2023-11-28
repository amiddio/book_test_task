from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomerSerializer
from .tasks import send_customer_register_email_task


class CustomerAPIView(APIView):
    """Представление для создания пользователей"""

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.save()

        # Асинхронная задача для отправки email-а
        send_customer_register_email_task.delay(data=data)

        return Response({'result': True}, status=status.HTTP_201_CREATED)
