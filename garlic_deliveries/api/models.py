from django.db import models


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
    type_amount = models.JSONField(default=list)
    # ja problēma ieviest json, tad relācija uz citu modeli
    address = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def get_status(self):
        return self.status
    
    def get_updated_at(self):
        return self.updated_at
    
    class Meta:
        permissions = [
            ("change_delivery_status", "Can change delivery status"),
        ]
    
    