from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import EnderecoSerializer
from .services import EnderecoService
from enderecos.domain.endereco import EnderecoClient
from google.protobuf.json_format import MessageToDict


class EnderecoViewSet(ViewSet):
    serializer_class = EnderecoSerializer

    def list(self, request, *args, **kwargs):
        enderecos_client = EnderecoClient()
        enderecos = enderecos_client.list()
        response = []
        for endereco in enderecos:
            response.append(MessageToDict(endereco))

        return Response(response)

    def create(self, request, *args, **kwargs):
        endereco = EnderecoClient()
        response = endereco.create(request.data)
        return Response(MessageToDict(response))
