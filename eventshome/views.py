from django.shortcuts import render
from .models import Eventhome

# Create your views here.
def home(request):
	events = Eventhome.objects
	return render(request, 'eventshome/home.html', {'events': events})