from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def adios(request):
    return HttpResponse("Adios")

def adulto(request,edad):
    if edad >= 18:
        return HttpResponse("Es mayor de edad")
    else:
        return HttpResponse("Es menor de edad")
