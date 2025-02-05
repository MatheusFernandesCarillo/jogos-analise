import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

db = pd.read_csv('https://raw.githubusercontent.com/MatheusFernandesCarillo/jogos-analise/refs/heads/main/Video_Games_Sales_as_at_22_Dec_2016.csv')

db.columns = ["Nome", "Plataforma", "Lançamento", "Genero", "Publicadora", "Vendas_EUA", "Vendas_Europa", "Vendas_Japão", "Vendas_Outros", "Vendas_Global", "Nota_Critica", "Contagem_Criticos", "Nota_Usuario", "Contagem_Usuarios", "Desenvolvedora", "Classificação"]

db_limpo = db.drop(columns=['Nota_Critica', 'Contagem_Criticos', 'Nota_Usuario', 'Contagem_Usuarios'])
