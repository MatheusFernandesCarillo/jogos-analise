import matplotlib.pyplot as plt
import seaborn as sns
from vendas_por_regiao import vendas, processar_vendas_generico

fig, axes = plt.subplots(3, 2, figsize=(15, 15))

#utiliza a função para ver as vendas de cada regiao, ordenado por genero
for ax, (regiao, (coluna, cor)) in zip(axes[:2, :].flatten(), vendas.items()):
    data = processar_vendas_generico(coluna, 'Genero') 
    
    #cria o grafico
    sns.barplot(x=coluna, y="Genero", data=data, ax=ax, color=cor)
    ax.set_title(f'Vendas {regiao.capitalize()}')
    ax.set_xlabel("")
    ax.set_xticklabels([]

#adiciona um grafico unico com as quatro regioes
ax_big = fig.add_subplot(3, 1, 3)
for regiao, (coluna, cor) in vendas.items():
    data = processar_vendas_generico(coluna, 'Genero')  # Agrupando por 'Genero'
    sns.barplot(x=coluna, y="Genero", data=data, color=cor, label=regiao, ax=ax_big)

ax_big.set_title('Vendas por Gênero - Comparação Geral')
ax_big.set_xlabel('Vendas')
ax_big.set_ylabel('Gênero')
ax_big.legend()

plt.tight_layout()
plt.show()
