from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import ReservationSerializer
from apps.core.models import Reservation
from rest_framework.response import Response
from rest_framework import status

class BookDay(APIView):

    def get(self, request):
        context = {
            "message":"GET NOT ALLOWED"
        }
        return Response(data=context, status=status.HTTP_200_OK)

    def post(self, request):
        context = {}
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            context["status"] = True
            context["message"] = "data added successfully"
            date=serializer.validated_data.get("date")
            dates = Reservation.objects.filter(date=date).exists()
            if dates:
                context["status"] = False
                context["message"] = "someone has already reserved in that day."
                return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(data=context, status=status.HTTP_201_CREATED)
        context["status"] = False
        context["message"] = "invalid request"
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
