from uuid import uuid4

from django.db import models


class Endereco(models.Model):
    cd_endereco = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column="cd_endereco",
    )
    cep = models.CharField("Cep", max_length=20)
    logradouro = models.CharField("Logradouro", max_length=200)
    bairro = models.CharField("Bairro", max_length=80)
    cidade = models.CharField("Cidade", max_length=80)
    estado = models.CharField("Estado", max_length=80)

    def __str__(self):
        return self.cidade
