from django.shortcuts import redirect, render
from .forms import *

# Create your views here.


def home_emp(request):
    return render(request, 'home_emp.html')

def leaveReq(request):
    form = LeaveRequestForm()

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('home_emp')
    context = {'form':form}
    return render(request, 'emp_leaveReq.html',context)

    

def leaveStatus(request):
    return render(request,'emp_leavestatus.html')