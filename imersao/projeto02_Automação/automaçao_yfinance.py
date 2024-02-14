import yfinance as yf
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
#import mouse
from time import sleep

# Solicita o código da ação ao usuário
codigo = input('Digite o código da ação desejada: ')

# Obtém os dados históricos da ação
dados = yf.Ticker(codigo).history("6mo")

# Extrai os preços de fechamento
fechamento = dados.Close
fechamento.plot()
print(fechamento)

# Calcula o máximo, mínimo e preço atual
maximo = fechamento.max()
minimo = fechamento.min()
atual = fechamento.iloc[-1]
print(f'máximo: {maximo}')
print(f'mínimo: {minimo}')
print(f'atual: {atual}')

# Exibe o gráfico
plt.show()

# Abre o navegador Chrome
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('chrome')
pyautogui.press('enter')
sleep(2)
pyautogui.click(x=871, y=457)
sleep(2)
pyautogui.click(x=502, y=63)
sleep(2)

# Abre o Gmail e preenche os campos
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=85, y=183)
sleep(1)
pyperclip.copy('liposuck09@gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
pyperclip.copy('Análise diária')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# Cria a mensagem com as análises
mensagem = f'''Prezado gestor,

Seguem as análises diárias da ação {codigo}:

Cotação máxima: {maximo}
Cotação mínima: {minimo}
Cotação atual: {atual}

Qualquer dúvida, estou à disposição.
'''
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
sleep(3)
pyautogui.click(x=1300, y=1004)

# Comentário de documentação para a linha abaixo
# while True:
#    print(mouse.get_position())
