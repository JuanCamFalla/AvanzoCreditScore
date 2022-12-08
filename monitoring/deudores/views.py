import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Deudor


def DeudorList(request):
    queryset = Deudor.objects.all()
    context = list(queryset.values('id', 'nombre', 'apellido', 'cedula', 'version'))
    return JsonResponse(context, safe=False)

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
