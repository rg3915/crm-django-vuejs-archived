from django.urls import path
# from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

urlpatterns = [
    path('employee/', c.employee_list),
    path('employee/<int:pk>/', c.employee_detail),
]
