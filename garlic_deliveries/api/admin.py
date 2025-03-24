from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils import formats
from django.utils.formats import date_format

from .models import Delivery


class DeliveryAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields read-only except status
        for field_name, field in self.fields.items():
            if field_name != 'status':
                field.disabled = True

    class Meta:
        model = Delivery
        fields = '__all__'


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address', 'status', 'get_created_at', 'get_updated_at')
    list_filter = ('status',)
    search_fields = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address')
    readonly_fields = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address', 'type_amount', 'created_at', 'updated_at')
    ordering = ('status', '-created_at')

    def get_created_at(self, obj):
        return date_format(obj.created_at, format="Y. \\g\\a\\d\\a j. F, H:i")
    get_created_at.admin_order_field = 'created_at'
    get_created_at.short_description = 'Izveidots'

    def get_updated_at(self, obj):
        return date_format(obj.updated_at, format="Y. \\g\\a\\d\\a j. F, H:i")
    get_updated_at.admin_order_field = 'updated_at'
    get_updated_at.short_description = 'Atjaunināts'

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False
        return request.user.has_perm('api.change_delivery_status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


