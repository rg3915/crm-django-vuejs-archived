from django.urls import include, path
from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

router = routers.DefaultRouter()
router.register('employee', c.EmployeeViewSet, base_name='employee')

urlpatterns = [
    path('user/', c.UserList.as_view()),
    path('', include(router.urls)),
]
