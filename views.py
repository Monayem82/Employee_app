from django.shortcuts import render,get_object_or_404

from .models import *

def Employee_view(request):
    employees=Employee.objects.all()

    contax={
        "employes":employees
    }
    return render(request,'employee_app/index.html',contax)

def Employee_edit_view(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    print(employee)

    contax={
        "employee":employee
    }
    return render(request,'employee_app/edit.html',contax)