import main
import jogos_genero.py

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
