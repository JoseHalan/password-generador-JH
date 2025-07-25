import tkinter as tk
from tkinter import ttk
import random
import string

def gerar_senha():
    tamanho = int(spin_tamanho.get())
    usar_letras = var_letras.get()
    usar_numeros = var_numeros.get()
    usar_simbolos = var_simbolos.get()

    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        resultado.set("Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choices(caracteres, k=tamanho))
    resultado.set(senha)

# Interface Gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas")

ttk.Label(janela, text="Tamanho da senha:").grid(column=0, row=0, padx=5, pady=5)
spin_tamanho = ttk.Spinbox(janela, from_=4, to=32, width=5)
spin_tamanho.grid(column=1, row=0)
spin_tamanho.set(12)

var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

ttk.Checkbutton(janela, text="Letras", variable=var_letras).grid(column=0, row=1, sticky='w')
ttk.Checkbutton(janela, text="Números", variable=var_numeros).grid(column=0, row=2, sticky='w')
ttk.Checkbutton(janela, text="Símbolos", variable=var_simbolos).grid(column=0, row=3, sticky='w')

ttk.Button(janela, text="Gerar Senha", command=gerar_senha).grid(column=0, row=4, columnspan=2, pady=10)

resultado = tk.StringVar()
ttk.Entry(janela, textvariable=resultado, width=35).grid(column=0, row=5, columnspan=2)

janela.mainloop()