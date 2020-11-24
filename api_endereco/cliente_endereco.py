import grpc
from endereco_proto import endereco_pb2, endereco_pb2_grpc


with grpc.insecure_channel("localhost:50051") as channel:
    stub = endereco_pb2_grpc.EnderecoControllerStub(channel)
    print("----- Create -----")
    request = {
        "cep": "49670000",
        "logradouro": "Rua 34",
        "bairro": "capucho",
        "cidade": "Malhada dos bois",
        "estado": "Sergipe",
    }
    response = stub.Create(
        endereco_pb2.Endereco(
            cep="49670000",
            logradouro="Rua 34",
            bairro="capucho",
            cidade="Malhada dos bois",
            estado="Sergipe",
        )
    )
    print(response, end="")
    print("----- List -----")
    for endereco in stub.List(endereco_pb2.EnderecoListRequest()):
        print(endereco, end="")

    print("----- Retrieve -----")
    response = stub.Retrieve(
        endereco_pb2.EnderecoRetrieveRequest(cd_endereco=response.cd_endereco)
    )
    print(response, end="")
