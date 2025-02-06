from main import db_limpo
import plotly.express as px

vendas_por_regiao_e_ano = db_limpo.groupby('Lançamento')[['Vendas_EUA', 'Vendas_Europa', 'Vendas_Japão', 'Vendas_Outros']].sum().reset_index()

# Crie o gráfico de linhas com Plotly Express
fig = px.line(vendas_por_regiao_e_ano, x='Lançamento', y=['Vendas_EUA', 'Vendas_Europa', 'Vendas_Japão', 'Vendas_Outros'],
             title='Variação de Vendas por Região ao Longo dos Anos',
             labels={'value': 'Vendas', 'Lançamento': 'Ano de Lançamento', 'variable': 'Região'})

fig.show()
