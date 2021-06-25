from django.db.models import fields
from apps.core.models import Reservation
from rest_framework import serializers

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'email', 'phone', 'date']
        model = Reservation

