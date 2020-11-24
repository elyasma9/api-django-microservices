from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import EnderecoSerializer
from .services import EnderecoService
from enderecos.domain.endereco import EnderecoClient

class EnderecoViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        enderecos_client = EnderecoClient()
        enderecos = enderecos_client.list()
        print(enderecos)
        return Response({"teste":"enderecos"})

    '''def create(self, request, *args, **kwargs):
        enderecos_client = EnderecoClient()
        endereco = enderecos_client.create()
        response = EnderecoSerializer(endereco)
        return response'''

