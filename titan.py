import pandas as pd

tit = pd.read_csv('titanic.csv') # leitura do arquivo 'titanic.csv'


tit  = tit[['Name', 'Age', 'Sex','Pclass','Survived']] #seleciona colunas específicas

tit.loc[(tit['Survived']==1) & (tit['Pclass'] == 1) & (tit['Sex'] == 'female')].to_csv('titanic_result.csv') #adiciona filtros, e cria um novo arquivo csv

