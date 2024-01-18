# Bibliotecas importadas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib_venn import venn2
from faker import Faker

# (1) Geração de dados com nome e pontuação
fake = Faker()
num_pessoas = 10
nomes = [fake.name() for _ in range(num_pessoas)]
pontuacoes = np.random.randint(10, 50, size=num_pessoas)

dados = pd.DataFrame({'Nome': nomes, 'Pontuação': pontuacoes})

# (2) Gravar os dados em um arquivo texto
dados.to_csv('dados.txt', index=False, sep='\t')

# (3) Recuperar os dados do arquivo texto
dados_recuperados = pd.read_csv('dados.txt', sep='\t')

# Visualizar histograma
plt.figure(figsize=(10, 6))
plt.hist(dados_recuperados['Pontuação'], bins=10, edgecolor='black')
plt.xlabel('Pontuação')
plt.ylabel('Probabilidades')
plt.title('Histograma das Pontuações')
plt.grid(True)
plt.show()

# Visualizar nuvem de palavras
text = ' '.join(dados_recuperados['Nome'])
wordcloud = WordCloud(width=800, height=400,
                      background_color='black').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nomes')
plt.show()
