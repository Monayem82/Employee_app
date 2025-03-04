from django.shortcuts import render

from .models import *

def Employee_view(request):
    employees=Employee.objects.all()

    contax={
        "employes":employees
    }
    return render(request,'employee_app/index.html',contax)
