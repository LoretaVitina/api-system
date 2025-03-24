import requests
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Delivery(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Gaida piegādes apstiprināšanu'),
        ('processing', 'Apstrādē pie piegādātāja'),
        ('shipped', 'Tiek piegādāts'),
        ('delivered', 'Piegādāts'),
        ('cancelled', 'Piegāde atcelta')
    )
    
    delivery_id_from_warehouse = models.CharField(max_length=100, null=False, unique=True, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    # nezinu, vai būs e-pasts, bet to ir viegli noņemt
    e_mail = models.EmailField(max_length=100, null=False, blank=False)
    # ja problēma ieviest json, tad relācija uz citu modeli
    type_amount = models.JSONField(default=list)
    address = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_status = self.status if self.pk else None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._original_status = self.status

    def get_status(self):
        return self.status
    
    def get_updated_at(self):
        return self.updated_at
    
    class Meta:
        permissions = [
            ("change_delivery_status", "Can change delivery status"),
        ]
    

@receiver(post_save, sender=Delivery)
def notify_status_change(sender, instance, created, **kwargs):
    """
    Signal to notify external API when delivery status changes
    Only triggers on updates, not on new deliveries
    """
    try:
        if not created and instance._original_status != instance.status:
            data = {
                'delivery_id_from_warehouse': instance.delivery_id_from_warehouse,
                'status': instance.status
            }
            
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(
                settings.STATUS_UPDATE_ENDPOINT,
                json=data,
                headers=headers,
                timeout=10  # Add timeout to prevent hanging
            )
            
            response.raise_for_status()  # Raises an exception for 4XX/5XX responses
            
    except requests.Timeout:
        print(f"Timeout while notifying status change for delivery {instance.delivery_id_from_warehouse}")
    except requests.RequestException as e:
        print(f"Failed to notify status change for delivery {instance.delivery_id_from_warehouse}: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    