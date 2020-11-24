import grpc
from google.protobuf import empty_pb2
from .models import Endereco
from .serializers import EnderecoSerializer
from endereco_proto.endereco_pb2_grpc import EnderecoControllerServicer
from endereco_proto.endereco_pb2 import Endereco as EnderecoProto


class EnderecoService(EnderecoControllerServicer):
    def List(self, request, context):
        enderecos = Endereco.objects.all()
        for endereco in enderecos:
            response = EnderecoSerializer(endereco)
            yield EnderecoProto(**response.data)

    def Create(self, request, context):
        serializer = EnderecoSerializer(request)

        # endereco_ctx = context
        # print("----CREATE----")
        # print(endereco_req)
        # print(endereco_ctx)
        # endereco_ctx_cad = Endereco.objects.create(**endereco_ctx)

        # return EnderecoProto(endereco_ctx_cad)
