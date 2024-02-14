import locale
from datetime import date
import calendar
from time import sleep
from fpdf import FPDF
pdf = FPDF()

# Classe para o PDF com imagem no cabeçalho
class PDFWithImage(FPDF):
    def header(self):
        self.image('Planner Controle Financeiro igreja.png',x=0, y=0, w=self.w, h=self.h)


# Configurar o locale para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Obter informações sobre o mês atual e anterior
ano = date.today().year
mes_atual = date.today().month
mes1 = calendar.month_name[mes_atual]
mes_anterior = mes_atual - 1 if mes_atual > 1 else 12
nome_mes_anterior = calendar.month_name[mes_anterior]

# Criação de strings para formatação
sublinhado = '---'*14
simbolo = ' R$'

# Imprimir cabeçalho
print(sublinhado)
print(f'Relatorio referente a {nome_mes_anterior}/{ano}')
print(sublinhado)
sleep(1)

# Entradas
print('-------Digite as entradas------')
dizimo = float(input('Dízimos: R$'))
ofertas = float(input('Ofertas: R$'))
oferta_alugel = float(input('Oferta especial p/ Alugel R$'))
cantina_bazar = float(input('Cantina/bazar R$'))

# Adicionar novas entradas dinamicamente
adicionar = ''
contador = 0
variaveis_criadas = []
while adicionar in 'sS':
    adicionar = str(input('+ Adicionar nova entrada? [S/N]:  '))
    if adicionar in 'Nn':
        break
    else:
        nome_nova_entrada = input('Nome da nova entrada:')
        valor_nova_entrada = float(input('Valor: R$'))
        variaveis_criadas.append((nome_nova_entrada, valor_nova_entrada))
        contador += 1

# Calcular totais de entradas
total_novas_entradas = sum(valor[1] for valor in variaveis_criadas)
total_entradas = dizimo + ofertas + oferta_alugel + \
    cantina_bazar+total_novas_entradas

# Imprimir detalhes das entradas
print(f'numero de novas entradas: {contador}')
print(sublinhado)
for entrada in variaveis_criadas:
    nome, valor = entrada
    print(f'{nome}: R${valor:.2f}')

print(f'Dízimos: R${dizimo:.2f}')
print(f'Ofertas: R${ofertas:.2f}')
print(f'Ofertas especiais p/ aluguel: R${oferta_alugel:.2f}')

print(sublinhado)
print(f'o Total de novas entradas sao R${total_novas_entradas:.2f}')
print(f'o Total de entradas é R${total_entradas:.2f}')

# despesas...........
print(sublinhado)
print('=-=-Despesas-=-=-')
print(sublinhado)

alugel_seguro_predial = float(input('Alugel/seguro predial: R$'))
cpfl = float(input('CPFL: R$'))
agua = float(input('Agua/esgoto: R$'))
prebenda = float(input('Prebenda: R$'))

# Adicionar novas despesas dinamicamente
variaveis_criadas2 = []
adicionar2 = ''
while adicionar2 in 'sS':
    adicionar2 = str(input('+ Adicionar nova despesa? [S/N]:  '))
    if adicionar2 in 'Nn':
        break
    else:
        nome_nova_saida = input('Nome da nova Despesa:')
        valor_nova_saida = float(input('Valor: R$'))
        variaveis_criadas2.append((nome_nova_saida, valor_nova_saida))
        contador += 1

# Calcular totais de despesas
total_novas_saidas = sum(valor[1] for valor in variaveis_criadas2)
total_saidas = alugel_seguro_predial+cpfl+agua+prebenda+total_novas_saidas

# Imprimir detalhes das despesas
print(f'numero de novas Despesas: {contador}')
print(sublinhado)
for saida in variaveis_criadas2:
    nome1, valor2 = saida
    print(f'{nome1}: R${valor2:.2f}')
print(f'aluguel/seguro Predial: R${alugel_seguro_predial}')
print(f'CPFL: R${cpfl}')
print(f'Agua: R${agua}')
print(f'Prebenda: R${prebenda}')
print(sublinhado)
print(f'o Total de novas Despesas é {total_novas_saidas}')
print(f'o Total de Despesas é {total_saidas}')
print(sublinhado)

# balanço do mes....
saldo_mes = total_entradas - total_saidas

# Imprimir detalhes das despesas
print('-=-=-=-Balanço do Mês-=-=-=-')
print(f'o Saldo do Mês é: R${saldo_mes:.2f}')

# Informações do mês anterior e acumulado
print('-=-=-=-Balanço do Geral-=-=-=-')
saldo_anterior = float(input('Saldo anterior: R$'))
saldo_acumulado = saldo_anterior + saldo_mes
print(f'O saldo acumulado é: R${saldo_acumulado}')

print('Gerando PDF...')

# Criar e configurar o PDF
pdf = PDFWithImage()
pdf.add_page()
pdf.set_font('Arial', 'B', size=8.8)

# entradas ...........................
# Adicionar detalhes das entradas ao PDF
pdf.text(151, 56, str(f'R${dizimo:.2f}'))
pdf.text(151, 63, str(f'R${ofertas:.2f}'))
pdf.text(151, 69, str(f'R${oferta_alugel:.2f}'))
pdf.text(151, 76, str(f'R${cantina_bazar:.2f}'))
for entrada_index, entrada1 in enumerate(variaveis_criadas):
    nome, valor = entrada1
    pdf.text(22.60, 82 + entrada_index*6, str(nome))
    pdf.text(151, 82+entrada_index*6, str(f'R${valor:.2f}'))

# saidas..............................
pdf.text(150, 114, str(f'R${alugel_seguro_predial:.2f}'))
pdf.text(150, 120, str(f'R${cpfl:.2f}'))
pdf.text(150, 126, str(f'R${agua:.2f}'))
pdf.text(150, 132, str(f'R${prebenda:.2f}'))
# ...

# Loop para as saídas
for entrada2_index, (nome1, valor2) in enumerate(variaveis_criadas2):
    pdf.text(22.62, 138 + entrada2_index * 6, str(nome1))
    pdf.text(150, 138 + entrada2_index * 6, str(f'R${valor2:.2f}'))

# ...

# balanço do mes....................
pdf.text(150, 182, str(f'R${total_entradas:.2f}'))
pdf.text(150, 188, str(f'R${total_saidas:.2f}'))
if saldo_mes < 1:
    pdf.set_text_color(255,0,0)
pdf.text(150, 194, str(f'R${saldo_mes:.2f}'))
pdf.set_text_color(0,0,0)

pdf.text(150, 234, str(f'R${saldo_anterior:.2f}'))
if saldo_mes < 1:
    pdf.set_text_color(255,0,0)
pdf.text(150, 239, str(f'R${saldo_mes:.2f}'))
pdf.set_text_color(0,0,0)

pdf.text(150, 245, str(f'R${saldo_acumulado:.2f}'))

pdf.set_text_color(255, 255, 255)
pdf.text(15, 15, str(f'{nome_mes_anterior}/{ano}'))
pdf.set_font('Arial', 'B', size=9)
pdf.set_text_color(0,0,255)
pdf.text(149.80, 98.10, str(f'{total_entradas:.2f}'))
pdf.text(149, 166.30, str(f'{total_saidas:.2f}'))

#salvando o pdf
pdf.output(f'relatorio_{mes_anterior}.pdf')
print('PDF gerado com sucesso!')
