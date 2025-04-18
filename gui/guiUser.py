import tkinter as tk
from products.products import Products

class MinhaTela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Tela com Botões - OOP")
        self.janela.geometry("400x300")
        self.janela.configure(bg="black")
        # Contadores
        self.contador_win = 1
        self.contador_lose = 1
        self.valueLose = 0
        self.entrada = 0
        self.resultado = 0
        self.entradaRow = 0
        self.products = Products()

        self.criar_componentes()


    def criar_componentes(self):
        fonte_label = ("Arial", 36, "bold")

        frame_labels = tk.Frame(self.janela, bg="black")
        frame_labels.pack(pady=(60, 30))

        self.label_win = tk.Label(frame_labels, text="", fg="lime", bg="black", font=fonte_label)
        self.label_win.pack(side="left", padx=30)

        self.label_lose = tk.Label(frame_labels, text="", fg="red", bg="black", font=fonte_label)
        self.label_lose.pack(side="left", padx=30)

        frame_botoes = tk.Frame(self.janela, bg="black")
        frame_botoes.pack(side="bottom", pady=10)

        cor_bordo = "#800000"

        botao1 = tk.Button(
            frame_botoes,
            text="WIN",
            command=self.botao1_clicado,
            width=15,
            height=2,
            bg=cor_bordo,
            fg="white",
            activebackground="gray",
            activeforeground="white"
        )
        botao1.pack(side="left", padx=10)

        botao2 = tk.Button(
            frame_botoes,
            text="LOSE",
            command=self.botao2_clicado,
            width=15,
            height=2,
            bg=cor_bordo,
            fg="white",
            activebackground="gray",
            activeforeground="white"
        )
        botao2.pack(side="left", padx=10)

                # Adiciona botão para definir entrada
        botao_set_entrada = tk.Button(
            self.janela,
            text="Set Entrada",
            command=self.abrir_janela_entrada,
            width=10,
            height=1,
            bg="gray20",
            fg="white"
        )
        botao_set_entrada.place(x=10, y=10)  # Posicionado no canto superior esquerdo

        # Label para mostrar a entrada atual
        self.label_entrada_atual = tk.Label(self.janela, text="Entrada: 000", fg="white", bg="black", font=("Arial", 12))
        self.label_entrada_atual.place(x=110, y=14)


    def botao1_clicado(self):
        print("botao", self.entrada, self.contador_win)
        total = self.products.calculo(self.entrada, self.contador_win)
        resultado = self.products.bruto(self.entrada, total)

        if self.contador_win > 2:
            self.contador_win = 0
            self.entrada = self.entradaRow
            self.label_lose.config(text=f"{self.entrada:.2f}")
            self.valueLose = 0
            self.contador_lose = 1
            total = 0

        self.label_win.config(text=f"{total:.2f}")
        self.contador_win += 1
        



        
    def botao2_clicado(self):
        self.contador_win = 1
        print(self.contador_lose)

        if  self.contador_lose == 1:
            self.valueLose += self.entrada

        elif  self.contador_lose == 2:
            self.entrada += (self.entrada * 15)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 3:
            self.entrada += (self.entrada * 40)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 4:
            self.entrada += (self.entrada * 40)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 5:
            self.entrada += (self.entrada * 30)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 6:
            self.entrada += (self.entrada * 30)/100
            self.valueLose += self.entrada
        
        elif  self.contador_lose == 7:
            self.entrada += (self.entrada * 25)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 8:
            self.entrada += (self.entrada * 30)/100
            self.valueLose += self.entrada
        
        elif  self.contador_lose == 9:
            self.entrada += (self.entrada * 40)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 10:
            self.entrada += (self.entrada * 50)/100
            self.valueLose += self.entrada

        elif  self.contador_lose == 11:
            self.entrada += (self.entrada * 35)/100
            self.valueLose += self.entrada

        self.label_lose.config(text=f"{self.entrada:.2f}")
        self.contador_lose += 1

    def abrir_janela_entrada(self):
        janela_input = tk.Toplevel(self.janela)
        janela_input.title("Definir Entrada")
        janela_input.geometry("250x120")
        janela_input.configure(bg="black")

        label = tk.Label(janela_input, text="Digite a entrada:", bg="black", fg="white")
        label.pack(pady=10)

        entrada_var = tk.StringVar()
        entrada_entry = tk.Entry(janela_input, textvariable=entrada_var)
        entrada_entry.pack()

        def confirmar():
            try:
                valor = float(entrada_var.get())
                self.entrada = self.products.calculoEntrada(valor)
                self.entradaRow = self.entrada 
                self.label_entrada_atual.config(text=f"Entrada: {valor}")
                janela_input.destroy()
            except ValueError:
                entrada_entry.delete(0, tk.END)
                entrada_entry.insert(0, "Valor inválido")

        botao_confirmar = tk.Button(janela_input, text="Confirmar", command=confirmar, bg="gray20", fg="white")
        botao_confirmar.pack(pady=10)


    def mainLoop(self):
        self.janela.mainloop()

