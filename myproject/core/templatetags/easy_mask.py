from django import template

register = template.Library()


@register.filter('cpf_mask')
def cpf_mask(cpf):
    if cpf:
        return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


@register.filter('cnpj_mask')
def cnpj_mask(cnpj):
    if cnpj:
        return '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])


@register.filter('cep_mask')
def cep_mask(cep):
    if cep:
        return '{}-{}'.format(cep[:5], cep[5:])
