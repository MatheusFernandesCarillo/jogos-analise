from main import db_notas
import matplotlib.pyplot as plt

#cria uma correlação entre notas e vendas 
correlation = db_notas['Nota_Critica'].corr(db_notas['Vendas_Global'])
print(f"Correlação entre Nota Crítica e Vendas Globais: {correlation}")

#remove os outliers
Q1 = db_notas['Vendas_Global'].quantile(0.25)
Q3 = db_notas['Vendas_Global'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

db_notas_sem_outliers = db_notas[
    (db_notas['Vendas_Global'] >= lower_bound) & (db_notas['Vendas_Global'] <= upper_bound)
]

#refaz a correlação sem os outliers
correlation_sem_outliers = db_notas_sem_outliers['Nota_Critica'].corr(db_notas_sem_outliers['Vendas_Global'])
print(f"Correlação entre Nota Crítica e Vendas Globais (sem outliers): {correlation_sem_outliers}")

#cria dois graficos, um com os outliers e um sem os outliers
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
plt.scatter(db_notas['Nota_Critica'], db_notas['Vendas_Global'])
plt.title('Nota Crítica vs. Vendas Globais (com outliers)')
plt.xlabel('Nota Crítica')
plt.ylabel('Vendas Globais')

plt.subplot(1, 2, 2)
plt.scatter(db_notas_sem_outliers['Nota_Critica'], db_notas_sem_outliers['Vendas_Global'])
plt.title('Nota Crítica vs. Vendas Globais (sem outliers)')
plt.xlabel('Nota Crítica')
plt.ylabel('Vendas Globais')

plt.tight_layout()
plt.show()
