# Generated by Django 3.2.12 on 2022-04-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteId',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('secret', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientePessoaNatural',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('nome_civil', models.CharField(max_length=255)),
                ('nome_social', models.CharField(max_length=255)),
                ('nome_marca', models.CharField(max_length=255)),
                ('nome_razaosocial', models.CharField(max_length=255)),
                ('cpf', models.IntegerField()),
                ('cnpj', models.IntegerField()),
                ('estado_civil', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoValorCredito',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('valor_cliente', models.FloatField()),
                ('credito_cliente', models.FloatField()),
                ('data_consulta', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropostaCredito',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('credito_cliente', models.FloatField()),
                ('credito_recomendado', models.FloatField()),
                ('credito_preaprov', models.FloatField()),
                ('credito_limite', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ValorCliente',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('renda_fixa', models.FloatField()),
                ('data_renda', models.DateField()),
                ('creditcard_valorfaturapg', models.FloatField()),
                ('data_creditcard', models.DateField()),
                ('contacorrente', models.CharField(max_length=255)),
                ('data_contacorrente', models.CharField(max_length=255)),
                ('contapoupanca', models.CharField(max_length=255)),
                ('data_contapoupanca', models.DateField()),
                ('valor_financiamento', models.FloatField()),
                ('valor_parcela_financiamento', models.FloatField()),
                ('data_inicio_financ_contrato', models.DateField()),
                ('data_fim_financ_contrato', models.DateField()),
                ('valor_emprestimo', models.FloatField()),
                ('valor_parcela_emprestimo', models.FloatField()),
                ('data_inicio_emprest_contrato', models.DateField()),
                ('data_fim_emprest_contrato', models.DateField()),
                ('patrimonios', models.FloatField()),
                ('data_patrimonios', models.DateField()),
                ('data_consulta', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValorClienteConjunto',
            fields=[
                ('clienteconjunto_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('cliente_id', models.CharField(max_length=50)),
                ('cliente_id2', models.CharField(max_length=50)),
                ('renda_fixa', models.FloatField()),
                ('data_renda', models.DateField()),
                ('creditcard_valorfaturapg', models.FloatField()),
                ('data_creditcard', models.DateField()),
                ('contacorrente', models.CharField(max_length=255)),
                ('data_contacorrente', models.CharField(max_length=255)),
                ('contapoupanca', models.CharField(max_length=255)),
                ('data_contapoupanca', models.DateField()),
                ('valor_financiamento', models.FloatField()),
                ('valor_parcela_financiamento', models.FloatField()),
                ('data_inicio_financ_contrato', models.DateField()),
                ('data_fim_financ_contrato', models.DateField()),
                ('valor_emprestimo', models.FloatField()),
                ('valor_parcela_emprestimo', models.FloatField()),
                ('data_inicio_emprest_contrato', models.DateField()),
                ('data_fim_emprest_contrato', models.DateField()),
                ('patrimonios', models.FloatField()),
                ('data_patrimonios', models.DateField()),
                ('data_consulta', models.DateField(auto_now_add=True)),
            ],
        ),
    ]