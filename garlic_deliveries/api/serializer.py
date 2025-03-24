from django.utils import timezone
from django.utils.formats import date_format
from rest_framework import serializers

from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        # typeamount pagaidām šeit nav, jo par to vēl nezinu
        fields = ['delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address']


# vēl vienu serializeri vajadzēs, lai izveidotu, ka parāda tikai statusu (varbūt arī updated_at)
class DeliveryStatusSerializer(serializers.ModelSerializer):
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ['status', 'updated_at']

    def get_updated_at(self, obj):
        if obj.updated_at:
            # Convert to local time and format
            local_time = timezone.localtime(obj.updated_at)
            return date_format(local_time, format="DATETIME_FORMAT")