from main import db_limpo

#cria uma função que agrupa, soma, e organiza as vendas
def processar_vendas_generico(coluna, agrupamento)
   if agrupamento not in db_limpo.columns:
        raise ValueError(f"A coluna de agrupamento '{agrupamento}' não existe no DataFrame.")
    
    vendas = db_limpo.groupby(agrupamento)[coluna].sum().reset_index()
    return vendas.sort_values(by=coluna, ascending=False)

#cria um dicionario com os dados
vendas = {
    "eua": ("Vendas_EUA", "blue"),
    "europa": ("Vendas_Europa", "green"),
    "japão": ("Vendas_Japão", "red"),
    "outros": ("Vendas_Outros", "orange")
}

