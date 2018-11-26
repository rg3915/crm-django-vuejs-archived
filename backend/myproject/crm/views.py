from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from .serializers import EmployeeSerializer, UserSerializer
from .models import Employee


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
