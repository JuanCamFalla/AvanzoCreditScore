from ..models import Deudor

def get_deudores ():
    queryset = Deudor.objects.all()
    return queryset

def get_deudor (id):
    deudor = Deudor.objects.raw('SELECT * FROM deudores_deudor WHERE cedula = %s', [id])
    return deudor

def create_deudor (nombre, apellido, cedula, telefono, direccion, email, version):
    deudor = Deudor(nombre=nombre, apellido=apellido, cedula=cedula, telefono=telefono, direccion=direccion, email=email, version=version)
    deudor.save()

def calcular_credito (id):
    return random.randint(0, 700)