# customers/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as needed

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
