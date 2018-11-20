from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'pk',
            'user',
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
