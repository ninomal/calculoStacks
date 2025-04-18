from gui.guiUser import MinhaTela
from products.products import Products

def main():
    tela = MinhaTela()
    tela.mainLoop()

    products = Products()
    print(products.calculoEntrada(150))


    print(products.calculo(products.calculoEntrada(150), 1))

    print(products.calculo(products.calculoEntrada(150), 2))

    print(products.bruto(products.calculoEntrada(150), products.calculo(products.calculoEntrada(150), 2)))


if __name__ == "__main__":
    main()