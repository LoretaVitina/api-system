from rest_framework import serializers

from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        # typeamount pagaidām šeit nav, jo par to vēl nezinu
        fields = ['warhouse_id', 'name', 'surname', 'e_mail', 'address']