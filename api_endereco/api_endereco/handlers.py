from .services import EnderecoService
from endereco_proto import endereco_pb2_grpc


def run(server):
    endereco_pb2_grpc.add_EnderecoControllerServicer_to_server(
        EnderecoService(),
        server
    )
