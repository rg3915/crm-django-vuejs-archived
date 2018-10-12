from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    ctx = {'mydebug': True}
    return render(request, 'index.html', ctx)


def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def configs(request):
    return render(request, 'configs.html')


@login_required
def configs_edit(request):
    return render(request, 'configs_edit.html')
