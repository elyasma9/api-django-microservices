import grpc
from endereco_proto import endereco_pb2, endereco_pb2_grpc


with grpc.insecure_channel("localhost:50051") as channel:
    stub = endereco_pb2_grpc.EnderecoControllerStub(channel)
    print("----- List -----")
    for endereco in stub.List(endereco_pb2.EnderecoListRequest()):
        print(endereco, end="")


