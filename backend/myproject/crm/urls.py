from django.urls import include, path
from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

router = routers.DefaultRouter()
router.register('employee', c.EmployeeViewSet)
router.register('employee/<int:pk>/', c.EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls))
]
