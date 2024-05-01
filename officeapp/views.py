from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Employee
from .form import Employeeform
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = Employeeform()
    return render(request, 'index.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html',{'employees':employees})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = Employeeform(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def delete(request, id):
    form = Employee.objects.get(id=id)
    form.delete()
    return redirect("/")

