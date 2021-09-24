from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('employee_list', views.employee_list, name='employee_list'),
    path('employee_new', views.employee_new, name='employee_new'),
    path('employee_delete/<int:pk>', views.employee_delete, name='employee_delete'),
    path('employee_edit/<int:pk>', views.employee_edit, name='employee_edit'),



]