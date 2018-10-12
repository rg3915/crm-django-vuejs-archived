from django.urls import include, path
from rest_framework import routers
from myproject.crm import views as c

app_name = 'crm'

router = routers.DefaultRouter()
router.register('employee', c.EmployeeViewSet)
router.register('employee/<int:pk>/', c.EmployeeViewSet)

# employee_contact_patterns = [
#     path('<int:pk>/', c.employee_contact, name='employee_contact'),
#     path('add/', c.employee_contact_create, name='employee_contact_add'),
#     path('<int:pk>/edit/', c.employee_contact_edit, name='employee_contact_edit'),
#     path(
#         '<int:pk>/delete/',
#         c.employee_contact_delete,
#         name='employee_contact_delete'
#     ),
# ]

# employee_phone_patterns = [
#     path('<int:pk>/', c.employee_phone, name='employee_phone'),
#     path('add/', c.employee_phone_create, name='employee_phone_add'),
#     path('<int:pk>/edit/', c.employee_phone_edit, name='employee_phone_edit'),
#     path(
#         '<int:pk>/delete/',
#         c.employee_phone_delete,
#         name='employee_phone_delete'
#     ),
#     path(
#         'ajax/load_phone_types/',
#         c.load_phone_types,
#         name='ajax_load_phone_types'
#     ),
# ]

# employee_bank_patterns = [
#     path('<int:pk>/', c.employee_bank, name='employee_bank'),
#     path('add/', c.employee_bank_create, name='employee_bank_add'),
#     path('<int:pk>/edit/', c.employee_bank_edit, name='employee_bank_edit'),
#     path(
#         '<int:pk>/delete/',
#         c.employee_bank_delete,
#         name='employee_bank_delete'
#     ),
# ]

# employee_patterns = [
#     path('contact/', include(employee_contact_patterns)),
#     path('phone/', include(employee_phone_patterns)),
#     path('bank/', include(employee_bank_patterns)),
#     # path('', c.EmployeeList.as_view(), name='employee_list'),
#     # path('add/', c.EmployeeCreate.as_view(), name='employee_add'),
#     # path('<int:pk>/', c.EmployeeDetail.as_view(), name='employee_detail'),
#     # path('<int:pk>/two/', c.EmployeeDetail2.as_view(), name='employee_detail2'),
#     # path('<int:pk>/edit/', c.EmployeeUpdate.as_view(), name='employee_update'),
#     path('<int:pk>/delete/', c.employee_delete, name='employee_delete'),
#     path(
#         'ajax/load_occupations/',
#         c.load_occupations,
#         name='ajax_load_occupations'
#     ),
# ]

urlpatterns = [
    # path('company/', include(company_patterns)),
    # path('provider/', include(provider_patterns)),
    # path('employee/', include(employee_patterns)),
    path('', include(router.urls))
]
