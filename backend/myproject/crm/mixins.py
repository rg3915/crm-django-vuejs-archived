from django.urls import reverse_lazy


class SuccessUrlMixin:
    pass

    # def get_success_url(self):
    #     obj, _ = self.model_name.objects.get_or_create(
    #         user=self.object,
    #     )
    #     kw = {'pk': obj.pk}
    #     return reverse_lazy(self.my_success_url, kwargs=kw)


class ModelName:
    '''Retorna o nome do model.'''

    def get_context_data(self, **kwargs):
        context = super(ModelName, self).get_context_data(**kwargs)
        context['modelname'] = self.model.__name__
        context['model_name'] = self.model._meta.verbose_name.title()
        context['model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context


# class CompanyContactFormMixin:

#     def get_context_data(self, **kwargs):
#         context = super(CompanyContactFormMixin,
#                         self).get_context_data(**kwargs)
#         context['form'] = CompanyContactForm()
#         return context
