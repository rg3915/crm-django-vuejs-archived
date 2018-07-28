from django.contrib.auth.views import login, logout
from django.urls import path
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        login,
        {
            'template_name': 'accounts/login.html',
            'authentication_form': LoginForm,
        },
        name='login'
    ),
    path('logout/', logout, name='logout'),
]
