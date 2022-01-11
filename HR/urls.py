from collections import namedtuple
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='home'),
    path('register_emp/',views.reg_emp, name='reg_emp'),
    path('emp_list',views.emp_list, name='emp_list'),
    path('pending_req',views.pending_req, name='pending_req'),
    path('approved_req', views.approved_req, name='approved_req'),
    path('approveLeave/<int:pk>', views.approveLeave, name='approveLeave')
]
