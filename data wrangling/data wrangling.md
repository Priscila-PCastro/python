###Data Wrangling

###Data wrangling com Python Pandas: Análise Exploratoria - Parte 1


“Manipulação de dados" ou "tratamento de dados".

Por que precisamos limpar dados?

Qualidade, Consistência, Integridade, Padronização, Melhor precisão, Melhor eficiência, Prevenção de viés, Conformidade com regulamentação 

Manipulando o dataframe para limpeza 

• Removendo colunas e linhas 

• Mudando index 

• Removendo duplicados


Lidando com dados faltosos (missing data)

Identificar Dados Ausentes: df.isna()
Remover Dados Ausentes:
Preencher Dados Ausentes:fillna()
Imputação Estatística:



###Transformação

Várias transformações podem ser aplicadas aos dados

Tratamento De Valores Ausentes
Codificação de Variáveis Categóricas
Normalização ou Padronização
Conversão de Tipos de Dados
Remoção De Dados Duplicados
Agregação de Dados
Criação De Novas Variáveis (Feature Engineering)
Divisão De Dados
Renomeação De Colunas
Mudança do Formato do DataFrame


import pandas as pd
import numpy as np




Ler o arquivo csv:


df = pd.read_csv("collected research people.csv")


Imprimir:


df.head()




df['Unnamed: 0']




df = df.drop(columns=['Unnamed: 0'])
df.head()




Alterar alguns nomes de colunas:


novas_cols = {'Endereerço': 'Endereço',
              'phone': 'Telefone',
              'anual_income': 'Renda Anual',
              'AAge': 'Idade',
              'n_filhos': 'N Filhos',
              'diariamente_sun blocker': 'Usa protetor solar diariamente',
              'Food_restrictions': 'Restrição alimentar',
              'streaming': 'Streaming'
              }


df.rename(columns=novas_cols, inplace=True)
df.head()


Visualizar a coluna nome
df.Nome
Expressão regular:
O \W equivale a [^a-zA-Zà-úÀ-Ú0-9_].


Remover os caracteres especiais


df.Nome.str.replace('\W', '')


Compara todos valores linha a linha a linha e o resultado vai ser true ou false
df.Nome.str.replace('\W', '')== df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9_]', '')


df.Nome = df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]', '')
df.head()




Visualizar a coluna telefone


df.Telefone


Removendo os caracteres especiais
df.Telefone.str.replace('[^0-9]', '')


Não substituir () e +-
df.Telefone.str.replace('[^0-9() +-]', '*')


Substituir o que era na por false


df.Telefone.str.contains('[*]', na=False)






