from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views import View
from myproject.crm.models import Company, Employee
from .models import Receipt, Expense, TypeExpense


class Financial(View):

    def get(self, request):
        template_name = 'financial/financial.html'
        return render(request, template_name)


def _dict_receipts(item):
    return dict(
        id=item.get('id'),
        description=item.get('description'),
        cost_center={
            'pk': item.get('cost_center'),
            'name': item.get('cost_center__social_name'),
        },
        expiration_date=item.get('expiration_date'),
        paid=item.get('paid'),
        paying_source={
            'pk': item.get('paying_source'),
            'name': item.get('paying_source__first_name'),
        },
        payment=item.get('payment'),
        payment_date=item.get('payment_date'),
        type_expense={
            'pk': item.get('type_expense'),
            'title': item.get('type_expense__title'),
        },
        value=item.get('value'),
        created=item.get('created'),
        modified=item.get('modified'),
        active=item.get('active'),
    )


# def receipts(request):
#     receipts = Expense.objects.filter(active=True)
#     data = serializers.serialize('json', receipts)
#     return HttpResponse(data, content_type='application/json')

def receipts(request):
    receipts = Expense.objects.filter(active=True)
    receipts = receipts.values(
        'id',
        'description',
        'cost_center',
        'cost_center__social_name',
        'expiration_date',
        'paid',
        'paying_source',
        'paying_source__first_name',
        'payment',
        'payment_date',
        'type_expense',
        'type_expense__title',
        'value',
        'created',
        'modified',
        'active',
    )
    data = [_dict_receipts(item) for item in receipts]
    return JsonResponse(dict(data=data))


# def paying_source(request):
#     paying_sources = Employee.objects.filter(active=True)
#     data = serializers.serialize('json', paying_sources)
#     return HttpResponse(data, content_type='application/json')


def _dict_paying_source(item):
    _name = (item.get('first_name'), item.get('last_name'))
    return dict(
        pk=item.get('pk'),
        name='{} {}'.format(_name[0], _name[1]),
    )


def paying_source(request):
    paying_sources = Employee.objects.filter(active=True)
    paying_sources = paying_sources.values('pk', 'first_name', 'last_name')
    data = [_dict_paying_source(item) for item in paying_sources]
    return JsonResponse(dict(data=data))


def type_expense(request):
    type_expenses = TypeExpense.objects.filter(active=True)
    type_expenses = type_expenses.values('pk', 'title')
    data = [dict(pk=item.get('pk'), title=item.get('title'))
            for item in type_expenses]
    return JsonResponse(dict(data=data))


def cost_center(request):
    cost_centers = Company.objects.filter(active=True)
    cost_centers = cost_centers.values('pk', 'social_name')
    data = [dict(pk=item.get('pk'), social_name=item.get('social_name'))
            for item in cost_centers]
    return JsonResponse(dict(data=data))
