from main import db_limpo

def extrair_franquia(nome_jogo):
    if not isinstance(nome_jogo, str):
        return "Outra"
    

    nome_jogo = nome_jogo.lower()
    
    franquias = {
        "Pokemon": ["pokemon", "pokémon"],
        "Mario": ["mario", "super mario"],
        "Call of Duty": ["call of duty", "cod"],
        "FIFA": ["fifa"],
        
    }
    
    for franquia, nomes in franquias.items():
        for nome in nomes:
            if nome in nome_jogo:
                return franquia
    
    return "Outra"  

db_limpo['Franquia'] = db_limpo['Nome'].apply(extrair_franquia)

vendas_por_franquia = db_limpo.groupby('Franquia')['Vendas_Global'].sum().reset_index()

vendas_por_franquia = vendas_por_franquia.sort_values(by='Vendas_Global', ascending=False)


media_vendas_por_franquia = db_limpo.groupby('Franquia')['Vendas_Global'].mean().reset_index()

# Ordenando as médias de vendas por franquia
media_vendas_por_franquia = media_vendas_por_franquia.sort_values(by='Vendas_Global', ascending=False)



print(f'O Total de vendas por franquia é\n{vendas_por_franquia}')
print(f'A Média de vendas por franquia é\n{media_vendas_por_franquia}')

def teste():
    print("Esse código não vai rodar automaticamente.")

if __name__ == "__main__":
    teste()  # Só executa se rodar vendas_franquia.py diretamente
