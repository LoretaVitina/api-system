from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Delivery


@receiver(post_migrate)
def create_delivery_manager_group(sender, **kwargs):
    if sender.name == 'api':
        # Create the group if it doesn't exist
        group, created = Group.objects.get_or_create(name='Delivery Managers')
        
        # Get the content type for Delivery model
        content_type = ContentType.objects.get_for_model(Delivery)
        
        # Get or create the custom permission
        custom_permission, created = Permission.objects.get_or_create(
            codename='change_delivery_status',
            name='Can change delivery status',
            content_type=content_type
        )
        
        # Get the default Django change permission
        change_permission = Permission.objects.get(
            codename='change_delivery',
            content_type=content_type
        )
        
        # Add both permissions to the group
        group.permissions.add(custom_permission)
        group.permissions.add(change_permission) 