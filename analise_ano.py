import plotly.express as px
from main import db_limpo

# Criando db_ano fora da função para que possa ser importado
db_ano = db_limpo.sort_values(by="Lançamento", ascending=False)
db_ano = db_ano.dropna(subset=['Lançamento'])
jogos_ano = db_ano.groupby('Lançamento')['Nome'].count().reset_index()
jogos_ano.rename(columns={'Nome': 'Quantidade de Jogos'}, inplace=True)

# Função para gerar o gráfico, pode ser chamada após importar db_ano
def gerar_grafico_ano():
    fig = px.line(jogos_ano, x='Lançamento', y='Quantidade de Jogos', title='Número de Jogos Lançados por Ano até 2016')
    fig.update_layout(xaxis_title='Ano de Lançamento', yaxis_title='Quantidade de Jogos')
    fig.show()

if __name__ == "__main__":
    gerar_grafico_ano()
