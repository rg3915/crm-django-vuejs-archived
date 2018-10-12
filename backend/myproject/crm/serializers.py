from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'pk',
            'personal_email',
            'slug',
            'photo',
            'birthday',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'cpf',
            'rg',
            'cnh',
            'cnpj',
            'imun',
            'ie',
            'internal',
            'occupation',
            'date_admission',
            'date_release',
            'salary',
            'active',
        )
