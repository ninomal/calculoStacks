class Products():
    def __init__(self):
        pass

    def calculoEntrada(self, entrada):
        entrada =  entrada/50
        return entrada

    def calculo(self, entrada,  win):
        print(entrada, win, "aquii")
        if win== 1:
            total = 0
            total = (entrada * 85)/100
            total += entrada
            print(total)
            return total

        else:
            total = 0
            entrada += (entrada * 85)/100 
            total = (entrada * 85)/100
            total += entrada
            return total

    def bruto(self, entrada, variavel):
        return variavel - entrada
    




        