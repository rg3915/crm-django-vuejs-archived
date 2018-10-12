from django.urls import include, path
from myproject.financial import views as f

app_name = 'financial'

financial_patterns = [
    path('', f.Financial.as_view(), name='financial'),
    path('receipts/', f.receipts, name='receipts'),
    path('paying_source/', f.paying_source, name='paying_source'),
    path('type_expense/', f.type_expense, name='type_expense'),
    path('cost_center/', f.cost_center, name='cost_center'),
]

urlpatterns = [
    path('financial/', include(financial_patterns)),
]
