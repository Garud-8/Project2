# support/views.py
from django.shortcuts import render
from customers.models import ServiceRequest

def manage_requests(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'support/manage_requests.html', {'service_requests': service_requests})
