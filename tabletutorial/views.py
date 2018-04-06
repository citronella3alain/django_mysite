from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable

# Create your views here.
def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    #return render(request, 'tabletutorial/people.html', {'people': Person.objects.all()})
    return render(request,'tabletutorial/people.html', {'table':table})
