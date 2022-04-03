# Generated by Django 3.2.12 on 2022-04-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientepessoanatural',
            name='cnpj',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clientepessoanatural',
            name='cpf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='historicovalorcredito',
            name='credito_cliente',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='historicovalorcredito',
            name='valor_cliente',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='propostacredito',
            name='credito_cliente',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='propostacredito',
            name='credito_limite',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='propostacredito',
            name='credito_preaprov',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='propostacredito',
            name='credito_recomendado',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='creditcard_valorfaturapg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_contapoupanca',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_creditcard',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_fim_emprest_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_fim_financ_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_inicio_emprest_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_inicio_financ_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_patrimonios',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='data_renda',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='patrimonios',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='renda_fixa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='valor_emprestimo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='valor_financiamento',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorcliente',
            name='valor_parcela_emprestimo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='creditcard_valorfaturapg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_contapoupanca',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_creditcard',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_fim_emprest_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_fim_financ_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_inicio_emprest_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_inicio_financ_contrato',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_patrimonios',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='data_renda',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='patrimonios',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='renda_fixa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='valor_emprestimo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='valor_financiamento',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='valor_parcela_emprestimo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='valorclienteconjunto',
            name='valor_parcela_financiamento',
            field=models.FloatField(null=True),
        ),
    ]
