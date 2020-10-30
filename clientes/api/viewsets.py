from rest_framework import viewsets

from clientes.api.serializers import ClienteSerializer, ContatoSerializer

from clientes.models import Cliente, Contato


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = Cliente.objects.all()
        return queryset


class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer

    def get_queryset(self):
        queryset = Contato.objects.all()
        return queryset
