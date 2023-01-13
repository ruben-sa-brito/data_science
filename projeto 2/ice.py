import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('IceCreamData.csv') #leitura do arquivo csv

x = [0,5,10,15,20,25,30,35] #lista com os valores da temperatura
z = -10
y= list()

for t in x: #itera sobre valores de cada faixa de temperatura
    temp = dados.loc[(dados['Temperature'] >= z) & (dados['Temperature'] < t)]
    z = t
    y.append(temp['Revenue'].sum())
    
    
plt.title('Vendas de sorvete')
plt.plot( x, y, 'r.--', label = 'US$')
plt.xlabel('Temperatura em °C')
plt.ylabel('Sales(US$)')
plt.legend()
plt.savefig('IceCream.pdf') #salva o gráfico em um arquivo pdf
plt.show()
