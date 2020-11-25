import grpc
from google.protobuf.empty_pb2 import Empty
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
        endereco_query = Endereco.objects.filter(
            cd_endereco=str(endereco.get("cdEndereco"))
        )
        if not endereco_query:
            return Empty()
        endereco_serializer = EnderecoSerializer(endereco_query.first())
        endereco_proto = EnderecoProto(**endereco_serializer.data)
        return endereco_proto

    # TODO: Retornar mensagem vazia pode ser um problema por causa do **CASO**
    # de objeto não encontrado
    def Destroy(self, request, context):
        endereco = MessageToDict(request)
        endereco_query = Endereco.objects.get(
            cd_endereco=str(endereco.get("cdEndereco"))
        )
        endereco_query.delete()
        return Empty()

    def Update(self, request, *args, **kwargs):
        endereco = MessageToDict(request)
        obj = Endereco.objects.filter(
            cd_endereco=endereco.get("cdEndereco")
        ).update(
            cep=endereco.get("cep"),
            logradouro=endereco.get("logradouro"),
            bairro=endereco.get("bairro"),
            cidade=endereco.get("cidade"),
            estado=endereco.get("estado"),
        )

        del endereco["cdEndereco"]
        endereco["cd_endereco"] = str(endereco.get("cdEndereco"))
        endereco_proto = EnderecoProto(**endereco)

        return endereco_proto
