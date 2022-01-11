from django.urls import path
from .import views


urlpatterns = [
    path('',views.home_emp, name='home_emp'),
    path('leaverequest/',views.leaveReq, name='leaveReq'),
    path('leavestatus/',views.leaveStatus, name='leaveStatus')
]
