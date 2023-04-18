from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('emp/<pk>', views.employee_form),
]
