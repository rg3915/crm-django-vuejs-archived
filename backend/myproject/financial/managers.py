from django.db import models


class ReceiptManager(models.Manager):
    ''' POSITIVO '''

    def get_queryset(self):
        return super(ReceiptManager, self).get_queryset().filter(value__gt=0)

    def active(self, **kwargs):
        return self.filter(active=True, **kwargs)


class ExpenseManager(models.Manager):
    ''' NEGATIVO '''

    def get_queryset(self):
        return super(ExpenseManager, self).get_queryset().filter(value__lt=0)

    def active(self, **kwargs):
        return self.filter(active=True, **kwargs)
