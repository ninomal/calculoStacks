import tkinter as tk
from products.products import Products

class MinhaTela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Tela com Botões - OOP")
        self.janela.geometry("800x600")
        self.janela.configure(bg="black")

        # Contadores e variáveis
        self.contador_win = 1
        self.contador_lose = 1
        self.valueLose = 0
        self.entrada = 0
        self.entradaRow = 0
        self.saldo_total = 0

        self.products = Products()

        self.criar_componentes()

    def criar_componentes(self):
        fonte_label = ("Arial", 100, "bold")

        # Frame dos labels de resultados
        frame_labels = tk.Frame(self.janela, bg="black")
        frame_labels.pack(pady=(60, 30))

        self.label_win = tk.Label(frame_labels, text="", fg="lime", bg="black", font=fonte_label)
        self.label_win.pack(side="left", padx=30)

        self.label_lose = tk.Label(frame_labels, text="", fg="red", bg="black", font=fonte_label)
        self.label_lose.pack(side="left", padx=30)

        # Frame dos botões principais
        frame_botoes = tk.Frame(self.janela, bg="black")
        frame_botoes.pack(side="bottom", pady=10)

        cor_botoes = "#800000"

        botao_win = tk.Button(
            frame_botoes, text="WIN", command=self.botao1_clicado,
            width=15, height=2, bg=cor_botoes, fg="white",
            activebackground="gray", activeforeground="white"
        )
        botao_win.pack(side="left", padx=10)

        botao_lose = tk.Button(
            frame_botoes, text="LOSE", command=self.botao2_clicado,
            width=15, height=2, bg=cor_botoes, fg="white",
            activebackground="gray", activeforeground="white"
        )
        botao_lose.pack(side="left", padx=10)

        # Botão para definir entrada
        botao_set_entrada = tk.Button(
            self.janela, text="Stop do Dia", command=self.abrir_janela_entrada,
            width=20, height=5, bg="yellow", fg="black",   font=("Arial", 20, "bold")
        )
        botao_set_entrada.place(x=10, y=300)

        # Label de entrada atual
        self.label_entrada_atual = tk.Label(self.janela, text="Stop do: 0.00", fg="white",
                                             bg="black", font=("Arial", 20))
        self.label_entrada_atual.place(x=40, y=14)

        # Label de saldo total
        self.label_saldo = tk.Label(self.janela, text="Saldo: 0.00",
                                     fg="cyan", bg="black", font=("Arial", 20, "bold"))
        self.label_saldo.place(x=400, y=14)

    def botao1_clicado(self):
        print("WIN", self.entrada, self.contador_win)
        total = self.products.calculo(self.entrada, self.contador_win)
        ganho = self.products.bruto(self.entrada, total)

        self.label_win.config(text=f"{total:.2f}")
        if self.contador_win > 2:
            if hasattr(self, 'label_win'):
                self.label_win.config(text="")
                print("limpou")

            self.contador_win = 0
            self.entrada = self.entradaRow
            self.label_lose.config(text=f"{self.entrada:.2f}")
            self.valueLose = 0
            self.contador_lose = 1
            ganho = 0  # Reset do ganho

        self.saldo_total += ganho
        self.label_saldo.config(text=f"Saldo: {self.saldo_total:.2f}")
        self.contador_win += 1

    def botao2_clicado(self):
        print("LOSE", self.contador_lose)

        # Tabela de percentuais de aumento por perda
        percentuais = [0, 0.15, 0.40, 0.40, 0.30, 0.30, 0.25, 0.30, 0.40, 0.50, 0.35]

        if self.contador_lose <= len(percentuais):
            aumento = percentuais[self.contador_lose - 1]
            self.entrada += (self.entrada * aumento)
            self.valueLose += self.entrada

            self.label_lose.config(text=f"{self.entrada:.2f}")
            self.saldo_total -= self.entrada
            self.label_saldo.config(text=f"Saldo: {self.saldo_total:.2f}")
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
                self.label_entrada_atual.config(text=f"Entrada: {valor:.2f}")
                janela_input.destroy()
            except ValueError:
                entrada_entry.delete(0, tk.END)
                entrada_entry.insert(0, "Valor inválido")

        botao_confirmar = tk.Button(janela_input, text="Confirmar", command=confirmar, bg="gray20", fg="white")
        botao_confirmar.pack(pady=10)

    def mainLoop(self):
        self.janela.mainloop()
