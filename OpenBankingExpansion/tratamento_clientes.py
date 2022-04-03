#----------------------------------------------------Bibliotecas-----------------------------------------------#
import pandas as pd
import base64
import os
from functools import reduce
#--------------------------------------------------------------------------------------------------------------#
#os.remove('TB_BASE_CLINTES.csv')    
def concatenar(nome_arquivo: str):
    df = pd.read_csv(nome_arquivo, sep ='\t')
    df['base'] = df['client_ID']+":"+df['secret']
    df['base'] = [base64.b64encode(x.encode('utf-8','string')) for x in df['base']]
    return df
#concatenar('Lista_Clientes_fake.csv')

def convertbase64(lista_base: list):
    return (base64.b64encode(lista_base), lista_base)

print(list(concatenar('D:\\Trabalho\\Projects\\SafraHackathon2022-Time16\\Lista_Clientes_fake.csv')))
