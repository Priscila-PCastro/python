
Introdução ao pandas 

O pandas, um pacote Python dedicado à manipulação de dados, também possuí funcionalidades para a visualização de dados. Sua estrutura é fundamentada em dois pacotes essenciais do Python: NumPy e Matplotlib. Enquanto o NumPy oferece objetos de matriz multidimensional para facilitar a manipulação de dados, o Matplotlib proporciona ao pandas capacidades robustas de visualização de dados.


Introdução ao DataFrames

imports pandas as pd

Criando um DataFrame - só tem 2 dimensões

df_cachorros = pd.DataFrame(dado) -> ond dados quer dizer um dicionarios 

primeiros métodos para entender seu DataFrame

df.head() - mostra as primeiras linhas da tabela

df_cachorro.head()

df.info() - mostra o que está dentro de cada coluna
df.shape- mostra quantas linhas e colunas tem
df.describe()- faz contas, devolve algumas estatísticas

componentes de uma DataFrame

Peças especiais de um DataFrame:

df.values: Valores
df.columns: as etiquetas (labs) das colunas
df.index: etiquetas das linhas

Ordenação e conjuntos

Você pode ordenar as linhas usando o método sort_values, passando o nome da coluna pela qual você deseja ordenar..

Ordenação:

df.sort_values(‘coluna’)- ordem do menor para o maior
Definir o argumento ascending como False ordenará os dados de forma inversa, do cachorro mais pesado para o cachorro mais leve..


df.sort_values(‘coluna, ascending = false’) - do maior para o menor


Podemos ordenar por várias variáveis passando uma lista de nomes de colunas para sort_values. 

Ordenação por múltiplas variáveis 

df.sort_values([‘Altura(cm)’, ‘Peso(kg)’])

Para alterar a direção da ordenação, passe uma lista para o argumento ascending para especificar em qual direção a ordenação deve ser feita para cada variável..

df.sort_values([‘Altura(cm)’, ‘Peso(kg)’],  ascending = [True, false])


Subconjunto de colunas

Subconjunto de várias colunas

Subconjunto de linhas

Subconjunto com base em dados de texto

Subconjunto com base em datas 

Subconjunto com base em múltiplas condições

Subconjunto usando .isin()

Adicionando uma nova coluna

Ler o arquivo csv
df = df.read_csv('carros.csv')
df.head()

Agregando dados



Extraindo estatística

Estatísticas resumidas, como o próprio nome sugere, são números que resumem e fornecem informações sobre seu conjunto de dados.

.median()
.mode()
.min()
.max()
.var()
.stad()
.sum()
.quantile()

O método de agregação, ou agg, permite calcular estatísticas personalizadas

.agg

i métodos para calcular estatísticas cumulativas. Chamar "cumsum" 

.cumcum()

O pandas também possui métodos para outras estatísticas cumulativas, como o máximo cumulativo, mínimo cumulativo e o produto cumulativo. Todos eles retornam uma coluna inteira de um DataFrame, em vez de um único número. 

.cumsum()
.cummax()
.cummin()
.comprod()


Lidando com valores duplicados

Excluindo duplicados

O método drop_duplicates do pandas remove linhas duplicadas de um DataFrame

drop_duplicates 


values_count()
normalize

Agrupando sem nenhum método de agrupamento

Usando groupby

Usando groupby com agg

Usando groupby com múltiplas variáveis

O que são tabelas pivot (ou dinâmicas)

pivot_table

Usando aggfunc

aggfunc

Substituir valores faltosos 
 fill_value


Índice e fatiando o dataframe

Alterando índices

.set_index(‘Nome’)

Removendo um index 

.reset_index()
.reset_index(drop=Ture)

Método loc - ajuda a pegar os pedaços do DataFrame

.loc[[ ‘ ‘ , ‘ ‘  ]]


Ordenando pelo valor do index

sort_index

Controlando o sort_index 

controlar a ordenação passando listas para os argumentos level e ascending

Slice usando Ioc 

O que é Slicing? Slicing é uma técnica para selecionar elementos consecutivos de objetos. Você também pode cortar DataFrames, mas primeiro precisa ordenar o índice. Aqui, o conjunto de dados de cachorros recebeu um índice de vários níveis de raça e cor; em seguida, o índice é ordenado com sort_index

Slice usando iloc


Gráficos, valores e faltosos 

Import matplotlib

A biblioteca básica de visualização de dados no Python é o matplotlib. Será melhor estudado no curso de visualização de dados com Python

from matplotlib import pyplot as plt

Lidando com valores faltosos 

Detectando valores nulos .isna() é um método que pode ser utilizado para encontrar os valores nulos. Retorna "True" para registros nulos. 

.isna()

E se o dataframe for maior? Como visualizar essa informação?

any
sum
plot

Removendo dados nulos 

O método dropna no pandas é utilizado para remover linhas ou colunas de um DataFrame 

 dropna

Substituindo valores nulos
 O método fillna no pandas é utilizado para preencher valores nulos (NaN) em um DataFrame com valores específicos. 
fillna

