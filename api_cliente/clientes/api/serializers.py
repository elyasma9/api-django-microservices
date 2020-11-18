from rest_framework import serializers
from clientes.models import Cliente, Contato


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["cd_cliente", "ddd", "numero", "email"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["cd_cliente", "nome", "sobrenome", "cpf", "sexo"]
