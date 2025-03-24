from django import forms
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db.models import Count
from django.utils import formats, timezone
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


class DeliveryStatusFilter(SimpleListFilter):
    title = 'status'  # Display name in the filter sidebar
    parameter_name = 'status'  # URL parameter name

    def lookups(self, request, model_admin):
        # Get all statuses with their counts
        status_counts = dict(
            Delivery.objects.values('status')
            .annotate(count=Count('status'))
            .values_list('status', 'count')
        )
        
        # Return list of tuples for all possible statuses
        return [
            (status_code, f"{status_label} ({status_counts.get(status_code, 0)})") 
            for status_code, status_label in Delivery.STATUS_CHOICES
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address', 'status', 'get_created_at', 'get_updated_at')
    list_filter = (DeliveryStatusFilter,)
    search_fields = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address')
    readonly_fields = ('delivery_id_from_warehouse', 'name', 'surname', 'e_mail', 'address', 'created_at', 'updated_at')
    ordering = ('status', '-created_at')

    def get_created_at(self, obj):
        # Convert UTC time to local time (Riga)
        local_time = timezone.localtime(obj.created_at)
        return date_format(local_time, format="Y. \\g\\a\\d\\a j. F, H:i")
    get_created_at.admin_order_field = 'created_at'
    get_created_at.short_description = 'Izveidots'

    def get_updated_at(self, obj):
        # Convert UTC time to local time (Riga)
        local_time = timezone.localtime(obj.updated_at)
        return date_format(local_time, format="Y. \\g\\a\\d\\a j. F, H:i")
    get_updated_at.admin_order_field = 'updated_at'
    get_updated_at.short_description = 'Atjaunināts'

    def get_queryset(self, request):
        # Allow all deliveries to be visible
        return super().get_queryset(request)

    def has_change_permission(self, request, obj=None):
        # Check for our custom permission instead of the default Django permission
        return request.user.has_perm('api.change_delivery_status')

    def has_view_permission(self, request, obj=None):
        # Also allow viewing if they have the status change permission
        return request.user.has_perm('api.change_delivery_status')

    def has_add_permission(self, request):
        # Optionally, restrict adding new deliveries
        return False

    def has_delete_permission(self, request, obj=None):
        # Optionally, restrict deleting deliveries
        return False


