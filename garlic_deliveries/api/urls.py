from django.urls import path

from .views import create_delivery, get_delivery, get_delivery_by_id

urlpatterns = [
    # ieviesu šo pathu tikai priekš testa, bet mums to nevajag
    path('delivery/', get_delivery, name='get_delivery'),
    # šis mums ir vajadzīgs, caur šo mūsu datubāzē ieglabāsies no warehouse dati
    path('delivery/create', create_delivery, name='create_delivery'),
    # šis mums būs priekš front-end, lai klients var meklēt pēc ID (ne mūsu datubāzes ID)
    # sliktākajā gadījumā warehouse var šo izmantot un ik pa laikam sūtīt pieprasījumus, bet tā parasti nedara
    path('delivery/<str:warhouse_id>', get_delivery_by_id, name='get_delivery_by_id'),
]