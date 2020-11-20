import grpc
from google.protobuf import empty_pb2
from .models import Endereco
from .serializers import EnderecoSerializer
from endereco_proto.endereco_pb2_grpc import EnderecoControllerServicer
from endereco_proto.endereco_pb2 import Endereco as EnderecoProto


class EnderecoService(EnderecoControllerServicer):
    def List(self, request, context):
        endereco = Endereco.objects.all()
        for endereco in enderecos:
            enderecos = EnderecoSerializer(endereco)
            yield EnderecoProto(**endereco)
