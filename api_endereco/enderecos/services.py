import grpc
from google.protobuf import empty_pb2
from .models import Endereco
from .serializers import EnderecoSerializer
from endereco_proto.endereco_pb2_grpc import EnderecoControllerServicer
from endereco_proto.endereco_pb2 import Endereco as EnderecoProto

from google.protobuf.json_format import MessageToDict


class EnderecoService(EnderecoControllerServicer):
    def List(self, request, context):
        enderecos = Endereco.objects.all()
        for endereco in enderecos:
            response = EnderecoSerializer(endereco)
            yield EnderecoProto(**response.data)

    def Create(self, request, context):
        endereco = MessageToDict(request)

        obj = Endereco.objects.create(
            cep=endereco.get("cep"),
            logradouro=endereco.get("logradouro"),
            bairro=endereco.get("bairro"),
            cidade=endereco.get("cidade"),
            estado=endereco.get("estado"),
        )
        endereco["cd_endereco"] = str(obj.cd_endereco)

        endereco_proto = EnderecoProto(**endereco)
        return endereco_proto

    def Retrieve(self, request, context):
        endereco = MessageToDict(request)
        endereco_query = Endereco.objects.get(cd_endereco=endereco.get("cd_endereco"))
        endereco_proto = EnderecoProto(**endereco_query)
        print(endereco_proto)
        return endereco_proto
