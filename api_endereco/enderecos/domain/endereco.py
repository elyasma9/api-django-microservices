import grpc
from endereco_proto import endereco_pb2_grpc, endereco_pb2
from enderecos.serializers import EnderecoSerializer


class EnderecoClient:
    def __init__(self):
        channel = grpc.insecure_channel("localhost:50051")
        self.stub = endereco_pb2_grpc.EnderecoControllerStub(channel)

    def list(self):
        enderecos = self.stub.List(endereco_pb2.EnderecoListRequest())
        for endereco in enderecos:
            yield endereco

    def create(self, request):
        print(request)
        endereco = self.stub.Create(
            endereco_pb2.Endereco(
                cep=request["cep"],
                logradouro=request["logradouro"],
                bairro=request["bairro"],
                cidade=request["cidade"],
                estado=request["estado"],
            )
        )

        return endereco

    def retrieve(self, pk):
        endereco = self.stub.Retrieve(
            endereco_pb2.EnderecoRetrieveRequest(cd_endereco=pk)
        )
        return endereco
