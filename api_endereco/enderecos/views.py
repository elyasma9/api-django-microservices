from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import EnderecoSerializer
from .services import EnderecoService


class EnderecoViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        enderecos = EnderecoService.List(request)
        response = EnderecoSerializer(enderecos)

        return Response(response.data)
