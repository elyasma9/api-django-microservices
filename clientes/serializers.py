from django_grpc_framework import proto_serializers
from clientes.models import Cliente
from cliente_proto import cliente_pb2


class ClienteProtoSerializer(proto_serializers.ProtoSerializer):
    class Meta:
        model = Cliente
        cliente_class = cliente_pb2
        fields = ['cd_cliente', 'nome', 'sobrenome', 'cpf', 'sexo',]
