class ActiveMixin:

    def get_queryset(self):
        queryset = super(ActiveMixin, self).get_queryset()
        queryset = queryset.filter(active=True)
        return queryset
