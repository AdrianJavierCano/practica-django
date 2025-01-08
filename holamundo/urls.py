from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", views.saludo, name='saludo'),
    path("adios/", views.adios, name='adios'),
    path("adulto/<int:edad>/", views.adulto, name='adulto')
]
