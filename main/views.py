from django.shortcuts import render, redirect
from main.models import Company, Employee
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def companies_view(request):
    companies = Company.objects.all()
    records = []
    for company in companies:
        data = {}
        employees = Employee.objects.filter(company=company.id)
        data['company'] = company
        data['employees'] = ", ".join([f'{emp.first_name} {emp.last_name}' for emp in employees])
        records.append(data)

    return render(request, 'companies.html', context={'data': records})


def employee_form(request, pk):
    if request.method == 'POST':
        try:
            emp_id = request.POST['emp']
        except MultiValueDictKeyError:
            return redirect(f'/emp/{pk}')

        employee = Employee.objects.get(id=emp_id)
        employee.company = Company.objects.get(id=pk)
        employee.save()
        return redirect('/')

    unemployed_employees = Employee.objects.filter(company__isnull=True)
    company = Company.objects.get(id=pk)
    context = {
        'employees': unemployed_employees,
        'company': company
    }
    return render(request, 'employee.html', context)
