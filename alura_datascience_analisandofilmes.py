# -*- coding: utf-8 -*-
"""Alura-DataScience-AnalisandoFilmes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EUCDyoA6b1TuqQhvxSZMSic3XpaXU4Sj
"""

print(sns.__version__)

"""**Analisando as notas em geral**"""

import pandas as pd

notas = pd.read_csv ('ratings.csv')

notas.head()

notas.shape

notas.columns = ["usuarioID","filmeID","nota","momento"]

notas.head()

notas['nota'].unique()

notas['nota'].value_counts()



notas['nota'].mean()

notas.nota.head()

notas.nota.plot(kind='hist')

print("Média =",notas['nota'].mean())
print("Mediana =",notas['nota'].median())

notas.nota.describe()

"""**Olhando os filmes**"""

import seaborn as sns

sns.boxplot(notas.nota)

filmes = pd.read_csv('movies.csv')
filmes.columns = ["FilmeID","Titulo","Genero"]
filmes.head()

"""#Analisando algumas notas específicas por Filme"""

notas.query("filmeID == 1").nota.mean()

notas.query("filmeID == 2").nota.mean()

Media_por_filme = notas.groupby("filmeID").mean().nota
Media_por_filme.head()

Media_por_filme.plot(kind='hist')

import matplotlib.pyplot as plt
plt.figure(figsize=(5,8))
sns.boxplot(y=Media_por_filme)

Media_por_filme.describe()

sns.distplot(Media_por_filme, bins=30)

import matplotlib.pyplot as plt
plt.hist(Media_por_filme)
plt.title("Histograma das médias dos Filmes")

tmdb = pd.read_csv('tmdb_5000_movies.csv')
tmdb.head()

tmdb.original_language.unique() #categorica nominal

tmdb.vote_average.unique()

contagem_de_lingua =tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingua.columns=("original_language","total")
contagem_de_lingua.head()

sns.barplot(x="original_language", y="total", data=contagem_de_lingua)

sns.catplot(x="original_language", kind="count", data=tmdb)

plt.pie(contagem_de_lingua["total"], labels= contagem_de_lingua["original_language"])

total_por_lingua =tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral-total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    'lingua': ['ingles','outros'],
    'total' : [total_de_ingles,total_do_resto]
}
dados=pd.DataFrame(dados)
sns.barplot(x="lingua", y="total", data=dados)

plt.pie(dados["total"], labels= dados["lingua"])

total_por_lingua_de_outros_filmes =tmdb.query("original_language!='en'").original_language.value_counts()
total_por_lingua_de_outros_filmes

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language!='en'")
sns.catplot(x="original_language", kind="count", data = filmes_sem_lingua_original_em_ingles,
            aspect = 2,
            palette = "GnBu_d",
            order = total_por_lingua_de_outros_filmes.index )

"""**REVISANDO MÉDIA, MEDIANA,DESVIO PADRÃO, DISPERSÃO, MEDIDAS DE TENDÊNCIA CENTRAL, BOXPLOT E HISTOGRAMA**"""

filmes.head(2)

notas_do_ToyStory = notas.query("filmeID==1")
notas_do_Jumanji = notas.query("filmeID==2")
print(len(notas_do_ToyStory),len(notas_do_Jumanji))

print("Nota média do Toy Story = %.2f "% notas_do_ToyStory.nota.mean())
print("Nota média do Jumanji = %.2f "% notas_do_Jumanji.nota.mean())

print("Nota média do Toy Story = %.2f "% notas_do_ToyStory.nota.median())
print("Nota média do Jumanji = %.2f "% notas_do_Jumanji.nota.median())

"""**Criando uma lista de 10 itens e tirando a média...como exemplo para aplicação**"""

import numpy as np
np.array([2.5]*10)

import numpy as np
np.array([2.5]*10).mean()

np.array([3.5]*10)

"""**Juntando os dois conjuntos (2.5 e 3.5) do exemplo**"""

filme1 = np.append (np.array([2.5]*10),np.array([3.5]*10))
filme2 = np.append (np.array([5]*10),np.array([1]*10))
filme1

filme2

"""**Média dos filmes 1 e 2 do exemplo**"""

print("Média do filme 1 = ", filme1.mean(),"Média do filme 2 = ",filme2.mean())

"""**Mediana dos filmes 1 e 2 do exemplo**"""

print("A Mediana do filme 1 é:",np.median(filme1),"  A Mediana do filme 2 é:",np.median(filme2))

"""**Analisando agora aplicado ao arquivo SNS**

Observe que não fica visualmente muito bom de analisar
"""

sns.distplot(filme1)
sns.distplot(filme2)

"""**Criando Histograma do arquivo SNS**"""

plt.hist(filme1)
plt.hist(filme2)

"""**Criando boxplot filme 1 e 2 do arquivo SNS em um array**"""

sns.boxplot([filme1, filme2])

"""**Analisando a distribuição dos fimes 1 e 2 (Toy Story e Jumanji**"""

sns.boxplot(x=notas_do_ToyStory.nota)
sns.boxplot(x=notas_do_Jumanji.nota)

plt.boxplot([notas_do_ToyStory.nota,notas_do_Jumanji.nota])

"""**Explorando a distribuição de todas as notas dos filmes 1 e 2:**"""

sns.boxplot(x="filmeID", y="nota", data=notas.query("filmeID in[1,2]"))

"""**Testando para mais filmes...**"""

sns.boxplot(x="filmeID", y="nota", data=notas.query("filmeID in[1,2,3,4,5]"))

"""**Analisando o desvio padrão**"""

print(notas_do_ToyStory.nota.std())

print(notas_do_Jumanji.nota.std())

print(np.std(filme1),np.std(filme2))