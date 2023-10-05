import matplotlib.pyplot as plt

def grafico_barra(moedas, valores):
    plt.bar(moedas, valores)
    plt.title("Conversões para Real (BRL)")
    plt.xlabel("Moedas")
    plt.ylabel("BRL (R$)")
    plt.show()

def grafico_pizza(moedas, valores):
    plt.pie(valores, labels = moedas)
    plt.title("Proporção em relação ao BRL - Real Brasileiro")
    plt.show()

def grafico_dispersao(moedas, valores):
    plt.scatter(moedas, valores)
    plt.title("Conversões para Real (BRL)")
    plt.xlabel("Moedas")
    plt.ylabel("BRL (R$)")
    plt.show()