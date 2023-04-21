from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Module
from .serializers import ModuleSerializer

class ModuleGetAll(generics.ListAPIView):

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleCreate(generics.CreateAPIView):

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class GetModule(APIView):

    def get(self, request, id):
        try:
            module = Module.objects.get(id=id)
            response = ModuleSerializer(module, many=False).data
        except ObjectDoesNotExist:
            response = {"status": "Объект не найден"}
        return Response(response)


class ModuleDelete(APIView):

    def delete(self, request, id):
        Module.objects.get(id=id).delete()
        return Response({"status": 200})

class UpdateModule(generics.UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


# Create your views here.
