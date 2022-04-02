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
    return df
#concatenar('Lista_Clientes_fake.csv')



