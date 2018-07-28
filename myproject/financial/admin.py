from django.conf import settings
from django.contrib import admin
from .models import Receipt, Expense, TypeExpense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    # objects = ExpenseManager()
    list_display = (
        '__str__',
        'payment_date',
        'paying_source',
        'type_expense',
        'cost_center',
        'expiration_date',
        'value',
        'payment',
        'paid',
        'active'
    )
    search_fields = (
        'description',
        'paying_source__first_name',
        'cost_center__first_name',
        'value',
    )
    list_filter = ('paid', 'paying_source', 'type_expense', 'active')
    # form = CompanyAdminForm
    actions = None

    if not settings.DEBUG:
        def has_add_permission(self, request, obj=None):
            return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    # objects = ReceiptManager()
    list_display = (
        '__str__',
        'payment_date',
        'paying_source',
        'type_expense',
        'cost_center',
        'expiration_date',
        'value',
        'payment',
        'paid',
        'active'
    )
    search_fields = (
        'description',
        'paying_source__first_name',
        'cost_center__first_name',
        'value',
    )
    list_filter = ('paid', 'paying_source', 'type_expense', 'active')
    # form = CompanyAdminForm
    actions = None

    if not settings.DEBUG:
        def has_add_permission(self, request, obj=None):
            return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TypeExpense)
class TypeExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active')
    search_fields = ('title', )
    list_filter = ('active',)
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False
