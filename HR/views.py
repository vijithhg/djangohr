from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import *
from Employee.models import LeaveRequest

# Create your views here.

def home(request):
    return render(request, 'home.html')

def reg_emp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'register_emp.html',context)


def emp_list(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request,'list_emp.html', context)

def pending_req(request):
    pending = LeaveRequest.objects.all().filter(status=False)
    context = {'pending':pending}
    return render(request,'pending_req.html',context)

def approved_req(request):
    approved = LeaveRequest.objects.all().filter(status = True)
    context = {'approved':approved}
    return render(request,'approved_req.html',context )

def approveLeave(request,pk):
    leaveStatus = LeaveRequest.objects.get(id=pk)
    leaveStatus.status = True
    leaveStatus.save()
    return redirect('approved_req')