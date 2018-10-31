from rest_framework import serializers
from django.contrib.auth.models import User
from newsocial_app.models import *


class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True,source="user.username")
    password = serializers.CharField(write_only=True,source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)
    perfil = serializers.CharField(required=False)


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('descripcion', 'id')
