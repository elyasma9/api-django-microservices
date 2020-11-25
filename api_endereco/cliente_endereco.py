import grpc
from endereco_proto import endereco_pb2, endereco_pb2_grpc


with grpc.insecure_channel("localhost:50051") as channel:
    stub = endereco_pb2_grpc.EnderecoControllerStub(channel)
    """print("----- Create -----")
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
        endereco_pb2.EnderecoRetrieveRequest(
            cd_endereco="cb87da3f-64fb-40a8-8df7-3752c95296bf"
        )
    )
    print(response, end="")

    print("------ Delete -------")
    response = stub.Destroy(
        endereco_pb2.Endereco(cd_endereco="cb87da3f-64fb-40a8-8df7-3752c95296bf")
    )
    print(response, end="")"""

    print("----- Update -----")
    response = stub.Update(
        endereco_pb2.Endereco(
            cd_endereco="f386f138-379d-484d-a902-7c913f8cf8f0",
            cep="49670000",
            logradouro="Rua 34",
            bairro="capucho",
            cidade="Malhada dos bois",
            estado="Sergipe",
        )
    )
    print(response, end="")
