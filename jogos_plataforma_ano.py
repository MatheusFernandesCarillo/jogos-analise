from analise_ano import db_ano
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Ver qual plataforma mais teve jogos ao longo dos anos
db_plataforma_ano = db_ano.groupby(['Lançamento', 'Plataforma'])['Nome'].count().reset_index()
db_plataforma_ano.rename(columns={'Nome': 'Quantidade de Jogos','Lançamento':' Ano de Lançamento'}, inplace=True)

# Ordena pela quantidade de jogos por plataforma, separando cada ano
db_plataforma_ano.sort_values(by='Quantidade de Jogos', ascending=False)

# Gráfico interativo, mostrando a quantidade de jogos por plataforma, ano a ano
fig2 = px.line(db_plataforma_ano, x=' Ano de Lançamento', y='Quantidade de Jogos', color='Plataforma', title='Comparação de Plataformas ao Longo dos Anos')
fig2.update_layout(xaxis_title='Ano de Lançamento', yaxis_title='Quantidade de Jogos')
fig2.show()

# Gráfico mostrando a quantidade de jogos por plataforma, somados
plt.figure(figsize=(15, 8))
sns.countplot(y="Plataforma", data=db_ano, order=db_ano['Plataforma'].value_counts().index)
plt.title('Quantidade de Jogos por Plataforma')
plt.show()
