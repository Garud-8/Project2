# support/models.py
from django.db import models

class SupportAgent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as needed
