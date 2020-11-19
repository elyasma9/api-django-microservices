from uuid import uuid4
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Cliente(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("-", "Prefiro não dizer"),
    ]
    cd_cliente = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column="cd_cliente",
    )
    nome = models.CharField("Nome", max_length=30)
    sobrenome = models.CharField("Sobrenome", max_length=50)
    cpf = models.CharField("CPF", max_length=14)
    sexo = models.CharField(
        "Sexo",
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=False,
    )
    endereco = models.PositiveIntegerField("Endereço")


class Contato(models.Model):
    cd_contato = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column="cd_contato",
    )
    cd_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    ddd = models.CharField("DDD", max_length=2, validators=[MinLengthValidator(2)])
    numero = models.CharField("Número", max_length=9)
    email = models.EmailField("Email", unique=True)
