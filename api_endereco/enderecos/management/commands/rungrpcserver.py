import grpc
from concurrent import futures
from django.core.management.base import BaseCommand, CommandError
from enderecos.services import EnderecoService
from endereco_proto import endereco_pb2_grpc



class Command(BaseCommand):
    help = "Comando para inicializar o serviço GRPC"

    def handle(self, *args, **options):
        self.stdout.write("Equipe Nasa")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        endereco_pb2_grpc.add_EnderecoControllerServicer_to_server(
            EnderecoService(), server
        )
        server.add_insecure_port('localhost:50051')
        server.start()
        server.wait_for_termination()
