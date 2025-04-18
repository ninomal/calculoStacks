class Products():
    def __init__(self):
        pass

    def calculoEntrada(self, entrada):
        entrada =  entrada/50
        return entrada

    def calculo(self, entrada,  win):
        if win== 1:
            total = (entrada * 85)/100
            total += entrada
            return total

        else:
            entrada += (entrada * 85)/100 
            total = (entrada * 85)/100
            total += entrada
            return total

    def bruto(self, entrada, variavel):
        return variavel - entrada
    




        