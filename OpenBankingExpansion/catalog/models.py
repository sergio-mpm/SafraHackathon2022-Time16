from datetime import datetime
from types import CellType
from django.db import connection
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

    def buscaClienteId(self, CPF_CNPJ: int):
        id_query = "SELECT DISTINCT cliente_id FROM dbo.catalog_clientepessoanatural WHERE CASE WHEN cpf IS NOT NULL THEN (REPLICATE('0', 14 - LEN(cpf)) + RTrim(cpf)) ELSE (REPLICATE('0', 14 - LEN(cnpj)) + RTrim(cnpj)) END = (REPLICATE('0', 14 - LEN(@cpf_cnpj)) + RTrim(@cpf_cnpj))"
        obj_valorcliente = ClientePessoaNatural.objects.raw(id_query)
        for obj in obj_valorcliente:
            cid = obj.cliente_id
        return cid


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

    def buscaClienteId(self, CPF_CNPJ: int):
        id_query = "SELECT DISTINCT cliente_id FROM dbo.catalog_clientepessoanatural WHERE CASE WHEN cpf IS NOT NULL THEN (REPLICATE('0', 14 - LEN(cpf)) + RTrim(cpf)) ELSE (REPLICATE('0', 14 - LEN(cnpj)) + RTrim(cnpj)) END = (REPLICATE('0', 14 - LEN(@cpf_cnpj)) + RTrim(@cpf_cnpj))"
        obj_valorcliente = ClientePessoaNatural.objects.raw(id_query)
        for obj in obj_valorcliente:
            cid = obj.cliente_id
        
        found_client = ValorCliente.vcmanager.filter(cid)


    # Entraria o algoritmo de cálculo de risco do Banco Safra para análise e retornaria o valor do cliente.
    def calcula_valor(self):
        ValorPositivoCliente = self.renda_fixa * 0.42
        self.data_consulta = datetime.now()
        self.save()
        return ValorPositivoCliente

    # Cálculo simulado de um crédito cedido ao cliente a partir das informações do OpenBanking.
    def calcula_credito(self):
        credito_cliente = PropostaCredito()
        credito_cliente.cliente_id = self.cliente_id
        credito_cliente.credito_limite = self.calcula_valor()
        credito_cliente.credito_recomendado = (self.calcula_valor()) * 0.7
        credito_cliente.credito_preaprov = (self.calcula_valor()) * 0.8
        credito_cliente.save()


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

    def calcula_valor(self):
        ValorPositivoCliente = ValorCliente.renda_fixa * 0.42
        return ValorPositivoCliente

    def calcula_credito(self):
        credito_cliente = PropostaCredito()
        credito_cliente.cliente_id = self.clienteconjunto_id
        credito_cliente.credito_limite = self.calcula_valor()
        credito_cliente.credito_recomendado = (self.calcula_valor()) * 0.7
        credito_cliente.credito_preaprov = (self.calcula_valor()) * 0.8
        credito_cliente.save()

    def concatena_valores(self, cliente1: ValorCliente, cliente2: ValorCliente):
        self.contacorrente = cliente1.contacorrente + cliente2.contacorrente
        self.contapoupanca = cliente1.contapoupanca + cliente2.contapoupanca
        self.creditcard_valorfaturapg = cliente1.creditcard_valorfaturapg + cliente2.creditcard_valorfaturapg
        self.renda_fixa = cliente1.renda_fixa + cliente2.renda_fixa
        self.valor_emprestimo = cliente1.valor_emprestimo + cliente2.valor_emprestimo
        self.valor_financiamento = cliente1.valor_financiamento + cliente2.valor_financiamento
        self.valor_parcela_emprestimo = cliente1.valor_parcela_emprestimo + cliente2.valor_parcela_emprestimo
        self.valor_parcela_financiamento = cliente1.valor_parcela_financiamento + cliente2.valor_parcela_financiamento
        self.patrimonios = cliente1.patrimonios + cliente2.patrimonios
        self.save()

    def gera_id_conjunto(self, cliente1: cliente_id, cliente2: cliente_id2):
        self.clienteconjunto_id = str(cliente1) +'_'+ str(cliente2)

    
class HistoricoValorCredito(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    valor_cliente = models.FloatField(null=True)
    credito_cliente = models.FloatField(null=True)
    data_consulta = models.DateField(auto_now_add=True)

    def registra_consulta(self, Consulta: ValorCliente):
        self.cliente_id = Consulta.cliente_id
        self.valor_cliente = Consulta.calcula_valor()
        self.credito_cliente = Consulta.calcula_credito()
        self.data_consulta = datetime.now()

    
class PropostaCredito(models.Model):
    cliente_id = models.CharField(max_length=50 ,primary_key=True, unique=True)
    credito_cliente = models.FloatField(null=True)
    credito_recomendado = models.FloatField(null=True)
    credito_preaprov = models.FloatField(null=True)
    credito_limite = models.FloatField(null=True)
