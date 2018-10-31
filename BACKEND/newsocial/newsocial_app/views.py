from django.shortcuts import render, render_to_response
from newsocial_app.models import *

from rest_framework import generics
from newsocial_app.serializers import *

from rest_framework.decorators import permission_classes
from newsocial_app.permissions import IsPostOrIsAuthenticated



def principal(request):
 return render_to_response("principal.html")

class RolList(generics.ListCreateAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()


class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

# Create your views here.

@permission_classes((IsPostOrIsAuthenticated,))

class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
