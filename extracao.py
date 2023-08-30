# Iniciando a leitura do arquivo csv

import pandas as pd
df = pd.read_csv ('backup_user.csv', sep = ';')

# Separando os dados relevantes

nomes = df['Nome']
datas = df['Data para backup']

# Extraindo dados e criando novo arquivo

nome_arquivo_saida = 'Notificacao.txt'

with open(nome_arquivo_saida, 'w') as arquivo_saida:
  for nome, data in zip(nomes, datas):
    frase = f"Bom dia {nome} o backup de dados de seu equipamento está agendado para {data} às 15:00hs.\nPor favor se programe para a visita do técnico.\n\n"
    arquivo_saida.write(frase)