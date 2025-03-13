from django.urls import path

from .views import create_delivery, get_delivery, get_delivery_by_id

urlpatterns = [
    path('delivery/', get_delivery, name='get_delivery'),
    path('delivery/create', create_delivery, name='create_delivery'),
    path('delivery/<str:warhouse_id>', get_delivery_by_id, name='get_delivery_by_id'),
]