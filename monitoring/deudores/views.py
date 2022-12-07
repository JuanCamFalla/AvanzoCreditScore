from django.shortcuts import render
from django.http import JsonResponse
from .models import Deudor


def DeudorList(request):
    queryset = Deudor.objects.all()
    context = list(queryset.values('id'))
    return JsonResponse(context, safe=False)


# Create your views here.
