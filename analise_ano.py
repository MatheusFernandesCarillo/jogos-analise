#importando o arquivo main
import main
import plotly.express as px

#ordenando pelo ano de lançamento dos jogos
db_ano = db_limpo.sort_values(by="Lançamento", ascending=False)
#retirando todos os jogos que não tenham ano de lançamento
db_ano = db_ano.dropna(subset= ['Lançamento'])

#organiza para mostrar apenas o ano do lançemento e a quantidade de jogos lançados
jogos_ano = db_ano.groupby('Lançamento')['Nome'].count().reset_index()
jogos_ano.rename(columns={'Nome': 'Quantidade de Jogos'}, inplace=True)

#cria um grafico interativo para mostrar os jogos, para poder ver os o ano em que mais saiu jogos
fig = px.line(jogos_ano, x='Lançamento', y='Quantidade de Jogos', title='Número de Jogos Lançados por Ano até 2016')
fig.update_layout(xaxis_title='Ano de Lançamento', yaxis_title='Quantidade de Jogos')
fig.show()
