from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Delivery
from .serializer import DeliverySerializer, DeliveryStatusSerializer


# šo mums nevajag, jo mums nekur nevajag parādīt visas piegādes
@api_view(['GET'])
def get_delivery(request):
    return Response(DeliverySerializer(Delivery.objects.all(), many=True).data)

@api_view(['POST'])
def create_delivery(request):
    # Check for password in Authorization header without 'Basic' prefix
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != settings.WAREHOUSE_PASSWORD:
        return Response(
            {"error": "Invalid credentials"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# šeit vajag atgriezt tikai statusu; jāizveido jauns serializeris
@api_view(['GET'])
def get_delivery_by_id(request, delivery_id_from_warehouse):
    try:
        delivery = Delivery.objects.get(delivery_id_from_warehouse=delivery_id_from_warehouse)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(DeliveryStatusSerializer(delivery).data)