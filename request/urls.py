from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^password/$', views.change_password, name='change_password'),
    path('req_new', views.req_new, name='req_new'),
    path('req_list', views.req_list, name='req_list'),
    path('admin_req_list', views.admin_req_list, name='admin_req_list'),
    path('req_approve/<int:pk>/', views.req_approve, name='req_approve'),
    path('req_delivered/<int:pk>/', views.req_delivered, name='req_delivered'),
    path('req_edit/<int:pk>', views.req_edit, name='req_edit'),
    path('req_delete/<int:pk>', views.req_delete, name='req_delete'),



]