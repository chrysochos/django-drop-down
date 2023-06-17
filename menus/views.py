from django.shortcuts import render
from menus.models import Person, District
import json

def my_view(request):
    persons = Person.objects.all()
    districts = District.objects.all()


    context = {
        'persons': persons,
        'districts': districts,
    }
    return render(request, 'webpage.html', context)
