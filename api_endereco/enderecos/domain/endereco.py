import grpc
from endereco_proto import endereco_pb2_grpc, endereco_pb2


class EnderecoClient:
    def __init__(self):
        channel = grpc.insecure_channel("localhost:50052")
        self.stub = endereco_pb2_grpc.EnderecoControllerStub(channel)

    def list(self):
        enderecos = self.stub.List(endereco_pb2.EnderecoListRequest())
        for endereco in enderecos:
            yield endereco

    def create(self):
        endereco = self.stub.Create(
            endereco_pb2.Endereco(
                cep="49160000",
                logradouro="Rua a 32",
                bairro="17 de outubro",
                cidade="Aracaju",
                estado="SERGIPE"
            )
        )

        return endereco
