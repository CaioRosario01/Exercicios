import tkinter as tk
from tkinter import *
from tkinter import simpledialog

def tamanho_palavra():

   Tamanho_palavra = simpledialog.askstring("Tamanho da palavra", "Digite qualquer coisa: ")
   tamanho = len(Tamanho_palavra)
   resultado_label.config(text=f"Tamanho da palavra: {tamanho}")

janela1 = Tk()
janela1.title("Verificando tamanho")

# Adicionando um botão à janela para chamar a função
botao = tk.Button(janela1, text="Calcular Tamanho", command = lambda: print("Tamanho da palavra:", tamanho_palavra()))
botao.grid(column=1, row=2)

#Adicionando um rótulo à janela para exibir o resultado
resultado_label = tk.Label(janela1, text= "Tamanho da palavra:")
resultado_label.grid(column=1 ,row= 3)
janela1.mainloop()