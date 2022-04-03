from django.db import models

class ClienteId(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    secret = models.CharField(max_length=100)

    # def tokenGen(self):


class ClientePessoaNatural(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    nome_civil = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255)
    nome_marca = models.CharField(max_length=255)
    nome_razaosocial = models.CharField(max_length=255)
    cpf = models.IntegerField(null=True)
    cnpj = models.IntegerField(null=True)
    estado_civil = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    data_nascimento = models.DateField()


class ValorCliente(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    renda_fixa = models.FloatField(null=True)
    data_renda = models.DateField(null=True)
    creditcard_valorfaturapg = models.FloatField(null=True)
    data_creditcard = models.DateField(null=True)
    contacorrente = models.CharField(max_length=255)
    data_contacorrente = models.CharField(max_length=255)
    contapoupanca = models.CharField(max_length=255)
    data_contapoupanca = models.DateField(null=True)
    valor_financiamento = models.FloatField(null=True)
    valor_parcela_financiamento = models.FloatField()
    data_inicio_financ_contrato = models.DateField(null=True)
    data_fim_financ_contrato = models.DateField(null=True)
    valor_emprestimo = models.FloatField(null=True)
    valor_parcela_emprestimo = models.FloatField(null=True)
    data_inicio_emprest_contrato = models.DateField(null=True)
    data_fim_emprest_contrato = models.DateField(null=True)
    patrimonios = models.FloatField(null=True)
    data_patrimonios = models.DateField(null=True)
    data_consulta = models.DateField(auto_now_add=True)

    # def calcula_valor(self):
        # TO DO

    # def calcula_credito(valor_cliente: integer):
        # TO DO


class ValorClienteConjunto(models.Model):
    clienteconjunto_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    cliente_id = models.CharField(max_length=50)
    cliente_id2 = models.CharField(max_length=50)
    renda_fixa = models.FloatField(null=True)
    data_renda = models.DateField(null=True)
    creditcard_valorfaturapg = models.FloatField(null=True)
    data_creditcard = models.DateField(null=True)
    contacorrente = models.CharField(max_length=255)
    data_contacorrente = models.CharField(max_length=255)
    contapoupanca = models.CharField(max_length=255)
    data_contapoupanca = models.DateField(null=True)
    valor_financiamento = models.FloatField(null=True)
    valor_parcela_financiamento = models.FloatField(null=True)
    data_inicio_financ_contrato = models.DateField(null=True)
    data_fim_financ_contrato = models.DateField(null=True)
    valor_emprestimo = models.FloatField(null=True)
    valor_parcela_emprestimo = models.FloatField(null=True)
    data_inicio_emprest_contrato = models.DateField(null=True)
    data_fim_emprest_contrato = models.DateField(null=True)
    patrimonios = models.FloatField(null=True)
    data_patrimonios = models.DateField(null=True)
    data_consulta = models.DateField(auto_now_add=True)

    # def calcula_valor(self):
        # TO DO

    # def calcula_credito(valor_cliente: integer):
        # TO DO

    # def concatena_valores(cliente1: ValorCliente, cliente2: ValorCliente)
        # TO DO

    # def gera_id_conjunto(cliente1: cliente_id, cliente2: cliente_id2)
        # TO DO

    
class HistoricoValorCredito(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    valor_cliente = models.FloatField(null=True)
    credito_cliente = models.FloatField(null=True)
    data_consulta = models.DateField(auto_now_add=True)

    # def registra_consulta(Consulta: ValorCliente):
        # TO DO

    
class PropostaCredito(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    credito_cliente = models.FloatField(null=True)
    credito_recomendado = models.FloatField(null=True)
    credito_preaprov = models.FloatField(null=True)
    credito_limite = models.FloatField(null=True)
