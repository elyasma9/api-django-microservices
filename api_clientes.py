import grpc
from cliente_proto import cliente_pb2, cliente_pb2_grpc


with grpc.insecure_channel('localhost:50051') as channel:
    stub = cliente_pb2_grpc.ClienteControllerStub(channel)
    print('----- Create -----')
    response = stub.Create(cliente_pb2.Cliente(nome='Harrison', sobrenome='Santos', cpf="00000000000", sexo="M",))
    print(response, end='')
    print('----- List -----')
    for cliente in stub.List(cliente_pb2.ClienteListRequest()):
        print(cliente, end='')
    print('----- Retrieve -----')
    response = stub.Retrieve(cliente_pb2.ClienteRetrieveRequest(id=response.id))
    print(response, end='')
    print('----- Update -----')
    response = stub.Update(cliente_pb2.Cliente(id=response.id, nome='Ian', cpf='11111111111'))
    print(response, end='')
    print('----- Delete -----')
    stub.Destroy(cliente_pb2.Cliente(id=response.id))
