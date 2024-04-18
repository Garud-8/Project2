# customers/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer/track_request.html', {'service_requests': service_requests})

