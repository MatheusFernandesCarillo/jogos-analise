from main import db_limpo
import matplotlib.pyplot as plt
import seaborn as sns
from vendas_franquia import extrair_franquia

db_limpo['Franquia'] = db_limpo['Nome'].apply(extrair_franquia)


db_franquias = db_limpo.dropna(subset=['Franquia'])

# Agrupa por franquia e ano de lançamento, somando as vendas globais
vendas_por_franquia_ano = db_franquias.groupby(['Lançamento', 'Franquia'])['Vendas_Global'].sum().reset_index()
vendas_por_franquia_ano = vendas_por_franquia_ano[vendas_por_franquia_ano['Franquia'] != 'Outra']

# Cria um gráfico de linhas para cada franquia
plt.figure(figsize=(12, 6))
for franquia in vendas_por_franquia_ano['Franquia'].unique():
    franquia_data = vendas_por_franquia_ano[vendas_por_franquia_ano['Franquia'] == franquia]
    sns.lineplot(x='Lançamento', y='Vendas_Global', data=franquia_data, label=franquia, marker='o')

plt.title('Vendas Globais por Franquia ao Longo dos Anos')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Vendas Globais')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

