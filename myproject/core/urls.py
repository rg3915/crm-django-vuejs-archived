from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('configs/', v.configs, name='configs'),
    path('configs/edit/', v.configs_edit, name='configs_edit'),
]
