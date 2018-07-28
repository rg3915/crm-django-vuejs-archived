from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    address_number = models.IntegerField('número', null=True, blank=True)
    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    district = models.CharField('bairro', max_length=100, blank=True)
    city = models.CharField('cidade', max_length=100, blank=True)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True


class Document(models.Model):
    cpf = models.CharField(
        'CPF',
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField('RG', max_length=11, null=True, blank=True)
    cnh = models.CharField('CNH', max_length=20, null=True, blank=True)
    cnpj = models.CharField(
        'CNPJ',
        max_length=18,
        unique=True,
        null=True,
        blank=True
    )
    imun = models.CharField(
        'Inscrição Municipal',
        max_length=12,
        null=True,
        blank=True
    )
    ie = models.CharField(
        'Inscrição Estadual',
        max_length=12,
        null=True,
        blank=True
    )
    oab = models.CharField('OAB', max_length=8, null=True, blank=True)
    oab_uf = models.CharField(
        'OAB UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True
