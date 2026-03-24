from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver, Manufacturer, Car

def index(request):
	all_drivers = Driver.objects.count()
	all_manufacturers = Manufacturer.objects.count()
	all_cars = Car.objects.count()
	context = {
		'num_drivers': all_drivers,
		'num_manufacturers': all_manufacturers,
		'num_cars': all_cars,
	}

	return render(request, 'taxi/index.html', context)
