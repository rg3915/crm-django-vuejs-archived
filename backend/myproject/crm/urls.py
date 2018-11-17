from django.urls import path
# from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

urlpatterns = [
    path('user/', c.UserList.as_view()),
    path('employee/', c.EmployeeList.as_view()),
    path('employee/<int:pk>/', c.EmployeeDetail.as_view()),
]
