Introdução a Numpy

Biblioteca central para computação científica 

Array
numpy.random.randint — NumPy v1.26 Manual

numpy.ma.zeros — NumPy v1.26 Manual

numpy.arange — Manual do NumPy v1.26

Importando Numpy

import numpy as np

Criando um numpy array do zero

np.zeros(2 , 2 ) - Qual a dimensão que vc quer do array e todos os elementos de serão zero((recebe uma tupla)), o primeiro número vai ser as linhas e o segundo as colunas
np.arange( )- valor inicial e valor final
np.random.random( ) - vc criar valores randômicos/ valores aleatórios
np.random.randint(10, 30 , size=((3, 5))) - valores aleatórios inteiros, limite inferior e superior


Por que usar numpy e não lista?

Usamos apenas uma tipo de dados no array
menos espaço na memória
Estrutura multidimensional, enquanto listas são unidimensionais

Arrays e mais dimensões 

Array 3d

Array vetor

shape(4,)
shape(4,1)- Para criar um array de vetor vertical e horizontal,número de linhas e número de colunas, separados por virgula

Um vetor 1 dimensão 

Matriz 2 dimensões
Tensor mais de 3 dimensões

Dimensões do array (atributos e métodos)


Manipulando Array

Index de uma array de 1 dimensão
Indexação = ordem, primeiro índice é sempre 0.
Começa: 0,1,2,3,4

Para index Array de duas dimensões usamos linha e coluna [L,C]

Para escolher uma linha inteira usa o [0]

Para pegar todos os valores de uma coluna usa o atributo vírgula(,) e dois pontos(:)

Cartela_bingo[ :,1]

Fatiar (slicing) um array de 1 dimensão, usa dois pontos(:) 

arr[2:4] - pega tudo da linha 2 até o 4 menos 1

Fatiar (slicing) um array de 2 dimensão

Ordenar (sorting) um array = Ordem

Eixo(axis)

axis 0 - linhas horizontais
axis1 - colunas vertical

Filtrando array


Indexação sofisticada(fancy indexing) e máscara (mask) em arry 2D

Fancy indexing e np.where()

Buscar e substituir

adicionando e removendo dados do array

Cálculos com arrays

Operações com Vetorização 
