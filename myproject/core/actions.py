from django.shortcuts import get_object_or_404


def _delete(model, pk):
    obj = get_object_or_404(model, pk=pk)
    obj.active = False
    obj.save()
