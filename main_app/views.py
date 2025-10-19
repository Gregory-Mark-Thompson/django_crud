from django.shortcuts import render
from .models import Army

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def army_index(request):
    armies = Army.objects.all()
    # Render the armies/index.html template with the armies data
    return render(request, 'armies/index.html', {'armies': armies})

def army_detail(request, army_id):
    army = Army.objects.get(id=army_id)
    return render(request, 'armies/detail.html', {'army': army})