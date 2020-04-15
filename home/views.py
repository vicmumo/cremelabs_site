from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #Function-based view
	# return HttpResponse('Homepage!')
    numbers= [1,2,3,4,5]
    name= 'Vic Mumo'

    args={'myName':name, 'Number': numbers}

    return render(request, 'home/index.html',args)