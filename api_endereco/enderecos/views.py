from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

from .serializers import EnderecoSerializer
from .services import EnderecoService
from enderecos.domain.endereco import EnderecoClient
from google.protobuf.json_format import MessageToDict

from .models import Endereco


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
        response = MessageToDict(response)

        return Response(response)

    def retrieve(self, request, pk=None):
        endereco = EnderecoClient()
        endereco_query = endereco.retrieve(pk)
        response = MessageToDict(endereco_query)

        return Response(response)

    def destroy(self, request, pk=None):
        endereco = EnderecoClient()
        endereco_query = endereco.destroy(pk)
        response = MessageToDict(endereco_query)

        return Response({"message": "Endereço excluído com sucesso"})

    def update(self, request, *args, **kwargs):
        endereco = EnderecoClient()
        response = endereco.update(request.data)
        response = MessageToDict(response)

        return Response(response)
