'''o código carrega dados de vendas de um arquivo Excel, cria histogramas para cada coluna selecionada e
salva esses histogramas como arquivos HTML individuais, exibindo-os e salvando-os com base no nome das colunas selecionadas.
'''
import pandas as pd
import plotly_express as px

# Carrega os dados do arquivo 'vendas.xlsx' em um DataFrame
dados = pd.read_excel('vendas.xlsx')

# Lista das colunas que serão usadas para gerar os gráficos
colunas = ['loja', 'cidade', 'estado', 'tamanho']

# Para cada coluna na lista 'colunas', gera um histograma de faturamento
# por coluna e salva o gráfico como um arquivo HTML
for coluna in colunas:
    # Cria um histograma usando Plotly Express, onde:
    # - x é a coluna atual de 'colunas'
    # - y é a coluna 'preco' (preço)
    # - title é o título do gráfico com a coluna atual
    # - text_auto exibe automaticamente os valores nos gráficos
    # - color é a coluna 'forma_pagamento' (forma de pagamento), usada para colorir os gráficos
    grafico = px.histogram(dados, 
                           x=coluna, 
                           y='preco', 
                           title=f'Faturamento por {coluna}', 
                           text_auto=True, 
                           color='forma_pagamento')
    
    # Exibe o gráfico
    grafico.show()
    
    # Salva o gráfico como um arquivo HTML com o nome 'faturamento-{coluna}-grafico.html'
    grafico.write_html(f'faturamento-{coluna}-grafico.html')
