import pandas as pd

tit = pd.read_csv('titanic.csv') # leitura do arquivo 'titanic.csv'


tit  = tit[['Name', 'Age', 'Sex','Pclass','Survived']] #seleciona colunas específicas

tit = tit.loc[(tit['Survived']==1) & (tit['Pclass'] == 1) & (tit['Sex'] == 'female')] #adiciona filtros

tit = tit.sort_values(['Name'], ascending= True) #organiza os dados em ordem alfabética 

tit.to_csv('titanic_result.csv') #cria um arquivo csv com as novas modificações