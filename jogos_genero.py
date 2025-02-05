import main

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
#mostra a lista
genero_agrupado
