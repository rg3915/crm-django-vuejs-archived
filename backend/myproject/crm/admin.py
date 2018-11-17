from django.utils.html import format_html
from django.contrib import admin
from .models import (
    Company,
    CompanyContact,
    Employee,
    EmployeeBankAccount,
    EmployeeContact,
    EmployeePhone,
    Occupation,
    Provider,
    ProviderContact,
)
from .managers import CompanyManager, ProviderManager


class CompanyInline(admin.TabularInline):
    model = CompanyContact
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyInline,)
    objects = CompanyManager()
    list_display = ('__str__', 'slug', 'email', 'active')
    # prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'social_name', 'email')
    list_filter = ('city',)
    # form = CompanyAdminForm
    actions = None

    # def has_add_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'email', 'phone', 'active')
    search_fields = ('company', 'name', 'email')
    list_filter = ('company', 'active')
    actions = None


class ProviderInline(admin.TabularInline):
    model = ProviderContact
    extra = 0


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    inlines = (ProviderInline,)
    objects = ProviderManager()
    list_display = ('__str__', 'slug', 'email', 'active')
    # prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'social_name', 'email')
    list_filter = ('city',)
    # form = ProviderForm
    actions = None

    # def has_add_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ProviderContact)
class ProviderContactAdmin(admin.ModelAdmin):
    list_display = ('provider', 'name', 'email', 'phone', 'active')
    search_fields = ('provider', 'name', 'email')
    list_filter = ('provider', 'active')
    actions = None


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'department')
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False


class EmployeeContactInline(admin.TabularInline):
    model = EmployeeContact
    extra = 0


class EmployeePhoneInline(admin.TabularInline):
    model = EmployeePhone
    extra = 0


class EmployeeBankInline(admin.TabularInline):
    model = EmployeeBankAccount
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeContactInline, EmployeePhoneInline, EmployeeBankInline)
    list_display = ('__str__', 'photo_img', 'slug', 'active')
    # readonly_fields = ('date_joined',)
    actions = None

    def photo_img(self, obj):
        if obj.photo:
            return format_html('<img width="32px" src="{}" />'.format(obj.photo.url))
    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


@admin.register(EmployeeContact)
class EmployeeContactAdmin(admin.ModelAdmin):
    list_display = ('employee', 'name', 'email', 'phone', 'active')
    search_fields = ('employee', 'name', 'email')
    list_filter = ('email', 'active')
    actions = None


@admin.register(EmployeePhone)
class EmployeePhoneAdmin(admin.ModelAdmin):
    list_display = ('employee', 'phone', 'phone_type', 'active')
    search_fields = ('employee',)
    list_filter = ('active',)
    actions = None


@admin.register(EmployeeBankAccount)
class EmployeeBankAccountAdmin(admin.ModelAdmin):
    list_display = ('employee', 'name', 'bank', 'agency', 'account', 'active')
    search_fields = ('name', 'bank', 'agency', 'account')
    list_filter = ('bank', 'active')
    actions = None
