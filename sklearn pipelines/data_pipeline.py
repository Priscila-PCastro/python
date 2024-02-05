import requests
import numpy as np
import pandas as pd
import logging
import schedule
import time

import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

headers = {"chave-api-dados" : "xxxxxxxxxxxx"}

def run_request(url_):
  resposta = requests.get(url_, headers=headers)
  return resposta.json()

def coletar_dados(url):
  logging.info('Pegou URL para a criação das diferentes URLs criando uma para cada página')
  list_urls = [url + str(i) for i in range(1, 6)]
  arr_urls = np.asarray(list_urls)

  vec_run = np.vectorize(run_request)
  logging.info('Fazendo uma requisição para cada URL')
  arr_responses = vec_run(arr_urls)
  logging.info('Requisições concluídas')
  arr_responses = arr_responses.tolist()
  reposta = np.concatenate(arr_responses).tolist()
  return reposta

def transformar_dado(dado):
  logging.info('Criando dataframe')
  # Insira o código para a criação do dataframe a partir do parâmetro 'dado'
  # A variável deve ter o nome df_area
  df = pd.DataFrame(dado)


  # Insita o log sobre o que está sendo executado, utilizando 'logging.info'
  logging.info('selecionando colunas')
  df_area = df[['funcao', 'valorEmpenhado']]

  # Insita o log sobre o que está sendo executado, utilizando 'logging.info'
  logging.info('Transformando dado string -> float')
  df_area['valorEmpenhado'] = df_area['valorEmpenhado'].str.replace('.', '').str.replace(',', '.').astype(np.float64)

  logging.info('Transformando dado string -> float')
  agg_area = df_area.groupby('funcao').sum('valorEmpenhado')

  logging.info('Transformando dados para retirar proporção em porcentagem')
  agg_area = agg_area['valorEmpenhado']/df_area['valorEmpenhado'].sum()
  agg_area = agg_area.reset_index()
  # Insira o código para reset de index de agg_area, usando reset_index()
  return agg_area

def carga(dado):
  dado.to_csv('distribuicao_empenho_area_2022.csv', index=True)
  # crie um arquivo CSV com p parâmetro 'dado', o nome do arquivo deve ser 'distribuicao_empenho_area_20220.csv'
  # esse método não tem retorno


# Escreva aqui quais são os passos para a extração dos dados e processamento
# Este método não tem retorno, no final será gerado um CSV com os dados a serem salvos

def etl():
  url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
  dado = coletar_dados(url)
  dado = transformar_dado(dado)
  carga(dado)
  # colete os dados
  # transforme os dados
  # salve os dados

# Executa ETL uma vez
etl()

#automação
# Agenda a execução diária do ETL
schedule.every().day.at('18:37').do(etl)

#Loop para executar continuamente
while True:
    schedule.run_pending()
    time.sleep(3600)
    print('....Rodou novamente...')
