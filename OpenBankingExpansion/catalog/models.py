from django.db import models

class clienteid(models.Model):
    cliente_id = models.TextField(primary_key=True)
    secret = models.TextField()

    class Meta:
        ordering = ['-cliente_id']

    # def tokenGen(self):


class ClientePessoaNatural(models.Model):
    cliente_id = models.TextField(primary_key=True)
    nome_civil = models.TextField()
    nome_social = models.TextField()
    nome_marca = models.TextField()
    nome_razaosocial = models.TextField()
    cpf = models.IntegerField()
    cnpj = models.IntegerField()
    estado_civil = models.TextField()
    sexo = models.TextField()
    nacionalidade = models.TextField()
    data_nascimento = models.DateField()

    class Meta:
        ordering = ['-cliente_id']


class ValorCliente(models.Model):
    cliente_id = models.TextField(primary_key=True)
    renda_fixa = models.FloatField()
    data_renda = models.DateField()
    creditcard_valorfaturapg = models.FloatField()
    data_creditcard = models.DateField()
    contacorrente = models.TextField()
    data_contacorrente = models.TextField()
    contapoupanca = models.TextField()
    data_contapoupanca = models.DateField()
    valor_financiamento = models.FloatField()
    valor_parcela_financiamento = models.FloatField()
    data_inicio_financ_contrato = models.DateField()
    data_fim_financ_contrato = models.DateField()
    valor_emprestimo = models.FloatField()
    valor_parcela_emprestimo = models.FloatField()
    data_inicio_emprest_contrato = models.DateField()
    data_fim_emprest_contrato = models.DateField()
    patrimonios = models.FloatField()
    data_patrimonios = models.DateField()
    data_consulta = models.DateField()

    class Meta:
        ordering = ['-cliente_id']

    # def calcula_valor(self):
        # TO DO

    # def calcula_credito(valor_cliente: integer):
        # TO DO


class ValorClienteConjunto(models.Model):
    clienteconjunto_id = models.TextField(primary_key=True)
    cliente_id = models.TextField()
    cliente_id2 = models.TextField()
    renda_fixa = models.FloatField()
    data_renda = models.DateField()
    creditcard_valorfaturapg = models.FloatField()
    data_creditcard = models.DateField()
    contacorrente = models.TextField()
    data_contacorrente = models.TextField()
    contapoupanca = models.TextField()
    data_contapoupanca = models.DateField()
    valor_financiamento = models.FloatField()
    valor_parcela_financiamento = models.FloatField()
    data_inicio_financ_contrato = models.DateField()
    data_fim_financ_contrato = models.DateField()
    valor_emprestimo = models.FloatField()
    valor_parcela_emprestimo = models.FloatField()
    data_inicio_emprest_contrato = models.DateField()
    data_fim_emprest_contrato = models.DateField()
    patrimonios = models.FloatField()
    data_patrimonios = models.DateField()
    data_consulta = models.DateField()

    class Meta:
        ordering = ['-cliente_id']

    # def calcula_valor(self):
        # TO DO

    # def calcula_credito(valor_cliente: integer):
        # TO DO

    # def concatena_valores(cliente1: ValorCliente, cliente2: ValorCliente)
        # TO DO

    # def gera_id_conjunto(cliente1: cliente_id, cliente2: cliente_id2)
        # TO DO

    
class HistoricoValorCredito(models.Model):
    cliente_id = models.TextField(primary_key=True)
    valor_cliente = models.FloatField()
    credito_cliente = models.FloatField()
    data_consulta = models.DateField()

    class Meta:
        ordering = ['-cliente_id']

    # def registra_consulta(Consulta: ValorCliente):
        # TO DO

    
class PropostaCredito(models.Model):
    cliente_id = models.TextField(primary_key=True)
    credito_cliente = models.FloatField()
    credito_recomendado = models.FloatField()
    credito_preaprov = models.FloatField()
    credito_limite = models.FloatField()

    class Meta:
        ordering = ['-cliente_id']
