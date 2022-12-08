import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Deudor
from .logic.logic_deudores import get_deudores
from .logic.logic_deudores import calcular_credito10
from .logic.logic_deudores import calcular_credito11
from django import template

register = template.Library()

def DeudorList(request):
    deudores = get_deudores()
    context = { 'deudores': deudores}
    return render(request, 'deudor/deudores.html', context)

def DeudorList2(request):
    deudores = Deudor.objects.all()
    return JsonResponse(list(deudores.values()), safe=False)

@register.simple_tag 
def calcularCreditScore(request):
    deudores = get_deudores()
    context = { 'deudores': deudores}
    for deudor in deudores:
        if deudor.version ==1.0:
            deudor.creditscore = calcular_credito10(id)
            deudor.save()
        elif deudor.version ==1.1:
            deudor.creditscore = calcular_credito11(id)
            deudor.save()
    return render(request, 'deudor/deudores.html', context)


    return


def CreateDeudor(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        nombre = data_json['nombre']
        apellido = data_json['apellido']
        cedula = data_json['cedula']
        telefono = data_json['telefono']
        direccion = data_json['direccion']
        email = data_json['email']
        version = data_json['version']
        deudor = Deudor(nombre=nombre, apellido=apellido, cedula=cedula, telefono=telefono, direccion=direccion, email=email, version=version)
        deudor.save()
        return JsonResponse({'status': 'ok'})
# Create your views here.
