from rest_framework.serializers import ModelSerializer
from .models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ["cd_endereco", "cep", "logradouro", "bairro", "cidade", "estado"]
