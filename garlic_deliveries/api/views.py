from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Delivery
from .serializer import DeliverySerializer


@api_view(['GET'])
def get_delivery(request):
    return Response(DeliverySerializer(Delivery.objects.all(), many=True).data)

@api_view(['POST'])
def create_delivery(request):
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_delivery_by_id(request, warhouse_id):
    try:
        delivery = Delivery.objects.get(warhouse_id=warhouse_id)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(DeliverySerializer(delivery).data)