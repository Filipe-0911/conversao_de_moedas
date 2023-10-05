from moedas import get_cotacao
from graficos import *

def menu():
    print()
    print("1 - Grafico de Barras: ")
    print("2 - Grafico de Pizza: ")
    print("3 - Grafico de Dispersão: ")
    print("0 - Sair")
    print()

opcao = 1
cotacoes = get_cotacao()

l_moedas = ["USD - Dólar", "EUR - Euro", "GBP - Libras"]
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

while opcao != 0:
    menu()
    opcao = int(input("Escolha um tipo de Gráfico: "))

    match opcao:
        case 1: grafico_barra(l_moedas, l_valores)
        case 2: grafico_pizza(l_moedas, l_valores)
        case 3: grafico_dispersao(l_moedas, l_valores)

print()
print("Até a próxima!")
print("Fim do script")