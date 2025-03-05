from django.shortcuts import render,get_object_or_404,redirect

from .models import *

def Employee_view(request):
    employees=Employee.objects.all()

    contax={
        "employes":employees
    }
    return render(request,'employee_app/index.html',contax)

def Employee_dashbord_view(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    print(employee)

    contax={
        "employee":employee
    }
    return render(request,'employee_app/edit.html',contax)


def Employee_edit_view(request,pk=None):
    employee = None
    if pk:
        employee=get_object_or_404(Employee,pk=pk)
    else:
        pk=None

    if request.method=="POST":
        if pk:
            employee.first_name=request.POST.get('first_name')
            employee.last_name=request.POST.get('last_name')
            employee.degignation=request.POST.get('degignation')
            employee.email=request.POST.get('email')
            employee.phone_number=request.POST.get('phone_number')
            employee.url=request.POST.get('url')
            if "profile_picture" in request.FILES:
                employee.image=request.FILES["image"]

            employee.save()

            return redirect("employe_edit", pk=pk)
        else:
            new_employee=Employee(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                degignation=request.POST.get('degignation'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                url=request.POST.get('url'),
                image=request.FILES.get("image"),
            )
            new_employee.save()
            return redirect("employe_index")
        
    contax={
        "employee":employee
    }
    return render(request,'employee_app/edit_up.html',contax)