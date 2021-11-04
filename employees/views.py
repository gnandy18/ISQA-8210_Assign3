from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


@login_required
def employee_list(request):
    employee = Employees.objects.filter(created_date__lte=timezone.now())
    return render(request, 'employee_list.html',
                  {'employees': employee})


@login_required
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)

            employee.save()
            employee = Employees.objects.filter()
            return render(request, 'employee_list.html',
                          {'employees': employee})
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    return redirect('employee_list')


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            employee.save()
            employee = Employees.objects.filter()
            return render(request, 'employee_list.html', {'employees': employee})
    else:
        # print("else")
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form})
