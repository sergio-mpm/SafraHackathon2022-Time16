#----------------------------------------------------Bibliotecas-----------------------------------------------#
import pandas as pd
import base64
import os
#--------------------------------------------------------------------------------------------------------------#
def concatenar_transformar_base64(nome_arquivo: str):
    df = pd.read_csv(nome_arquivo, sep ='\t')
    df1= list(df['client_ID']+":"+df['secret'])
    df['base'] = [str(base64.b64encode(x.encode('utf-8','string')))[2:-1] for x in df1]

    return (df)
def gerar_arquivo(dataframe: pd.DataFrame):
    dataframe.to_csv('TB_BASE_CLINTES.csv')
    print("TB_BASE_CLINTES.csv gerado corretamente")
    print(dataframe.head())
    pass
gerar_arquivo(concatenar_transformar_base64('C:\\Users\\DELL\\Documents\\Projeto_Safra\\SafraHackathon2022-Time16\\Lista_Clientes_fake.csv'))








