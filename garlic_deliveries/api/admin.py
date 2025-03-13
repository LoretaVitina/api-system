from django.contrib import admin

from .models import Delivery


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['warhouse_id', 'name', 'surname', 'e_mail', 'address', 'status', 'created_at', 'updated_at']
    # list_filter = ['status']
    # search_fields = ['warhouse_id', 'name', 'surname', 'e_mail', 'address']
    # readonly_fields = ['warhouse_id', 'name', 'surname', 'e_mail', 'address', 'created_at', 'updated_at']
    # list_filter = ['status']
    # ordering = ['created_at']

admin.site.register(Delivery)


