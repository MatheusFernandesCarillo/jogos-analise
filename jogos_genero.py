from main import db_limpo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#retira os valores nulos no genero
db_genero = db_limpo.dropna(subset= ['Genero'])

#ordena por genero
db_genero.sort_values('Genero')

#ordena e soma as vendas gerais por genero
genero_vendas = db_genero.groupby('Genero')['Vendas_Global'].sum().reset_index()
#ordena a quantidade de jogos por genero
genero_quantidade = db_genero.groupby('Genero')['Nome'].count().reset_index()
#renomeia a coluna
genero_quantidade = genero_quantidade.rename(columns={'Nome': 'Quantidade'})
#junta as duas colunas (vendas e quantidade)
genero_agrupado = pd.merge(genero_vendas, genero_quantidade, on='Genero')
#ordena por vendas
genero_agrupado = genero_agrupado.sort_values(by='Vendas_Global', ascending=False)

#agrupa por genero e ano de lançamento, somando as vendas globais
vendas_por_genero_ano = db_genero.groupby(['Lançamento', 'Genero'])['Vendas_Global'].sum().reset_index()

#encontra o genero mais lucrativo em cada ano
genero_mais_lucrativo_por_ano = vendas_por_genero_ano.loc[vendas_por_genero_ano.groupby('Lançamento')['Vendas_Global'].idxmax()]

#gráfico de linha mostando as mudanças ao longo dos anos
plt.figure(figsize=(12, 6))
sns.lineplot(x='Lançamento', y='Vendas_Global', hue='Genero', data=genero_mais_lucrativo_por_ano, marker='o')
plt.title('Gênero Mais Lucrativo por Ano')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Vendas Globais')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




