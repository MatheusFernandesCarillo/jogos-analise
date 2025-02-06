from vendas_por_regiao import vendas, processar_vendas
import matplotlib.pyplot as plt
import seaborn as sns

# Criando a figura e os eixos
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Iterando sobre os dados para criar os gráficos
for ax, (regiao, (coluna, cor)) in zip(axes.flat, vendas.items()):
    dados = processar_vendas(coluna)
    sns.barplot(x=coluna, y="Nome", data=dados.head(10), ax=ax, color=cor)
    ax.set_title(f'Vendas {regiao}')

# Ajustando layout
plt.tight_layout()
plt.show()
