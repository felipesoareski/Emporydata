import pandas as pd 
#carrega os dados
dados = pd.read_excel('vendas.xlsx')
#mostra as 5 primeiras linhas, pode colocar a quantidade de linhas dentro do parentes
primeiras_linhas = dados.head()
#mostra as ultimas linhas
ultimas_linhas = dados.tail()

print(primeiras_linhas)
print(ultimas_linhas)
#gerando estatisticas
print(dados.preco.describe())
#verifica os tipos de dados
#info = primeiras_linhas, ultimas_linhas.info()
#print('aki ta as info',info)

#total de vendas por loja
print(dados.loja.value_counts())

#total de vendas por cidade
print(dados.cidade.value_counts())

#total de vendas por forma de pagamento
print(dados.forma_pagamento.value_counts())

#agrupamento de dados
print(dados.groupby(['loja','cidade','estado']).preco.sum().to_excel('daturamento_estado_cidade.xlsx'))