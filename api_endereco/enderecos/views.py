from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import EnderecoSerializer
from .services import EnderecoService
from enderecos.domain.endereco import EnderecoClient

class EnderecoViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        enderecos_client = EnderecoClient()
        # endereco = enderecos_client.create()
        # print(endereco)
        # enderecos = enderecos_client.list()
        # for endereco in enderecos:
            # print(endereco)
            # print(endereco.message)
            # response = EnderecoSerializer(endereco)
            # print(response)
        return Response({"status": "OK"})
