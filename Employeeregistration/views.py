from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    context={'employee_list': Employee.objects.all()} # this is for getting the data from employee form and showing it on employee list page 
    return render(request,"employee_list.html",context)# this will retun render request for employee list.


def employee_form(request,id=0):# this function for employee form and id initialize to 0, this form perform both insert and update operation. 
    if request.method == "GET": # this if for get operation here i used get method
        if id ==0:# if id = 0 it means its for insert operation.
            form=EmployeeForm()# for insert I used employee form
        else: # This else for update operation.
            employee=Employee.objects.get(pk=id)# Here it will get data from database according to id, and id = pk(primary key)
            form=EmployeeForm(instance=employee)# here used Employee for and instance of employee
        return render(request,"employee_form.html",{'form':form})# This one to render the request to employee_form.html
    else:# This else part for POST operation
        if id ==0: # if id = 0, means for insert 
            form=EmployeeForm(request.POST)#And this form to get post request
        else:# this else part for update operation.
            employee=Employee.objects.get(pk=id)# Here it will data from database, according to id
            form=EmployeeForm(request.POST,instance=employee)#Here it will use employee form and get POST request
        if form.is_valid():# Here it will validate form
            form.save()#Here it will save form
        return redirect('/employee/list')# And this one to redirect this form to /employee/list


def employee_delete(request,id):# This for delete
    employee=Employee.objects.get(pk=id)# here it will get data from id into employee, pk and id both are same
    employee.delete()# here it will delete
    return redirect('/employee/list')#this will redirect to employee  list page after deletion.