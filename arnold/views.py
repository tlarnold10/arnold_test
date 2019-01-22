from django.shortcuts import render
import datetime

def homepage(request):
	hour = datetime.datetime.now().hour
	if hour >= 0 and hour <= 11:
		context = 'Good morning,'
	elif hour >= 12 and hour <= 17:
		context = 'Good afternoon,'
	else:
		context = 'Good evening,' 
	return render(request, 'index.html', {'time':context})

def aboutpage(request):
	return render(request, 'about.html')