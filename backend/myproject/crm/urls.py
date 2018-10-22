from django.urls import path
from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

router = routers.DefaultRouter()
router.register('employee/', c.Employee)

# urlpatterns = [
#     path('employee/', c.EmployeeList.as_view()),
#     path('employee/<int:pk>/', c.EmployeeDetail.as_view()),
# ]
