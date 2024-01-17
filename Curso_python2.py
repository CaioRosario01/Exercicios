#0- Projeto calculadora-interface.
#1- Importar o Tk inter.
#2- Importar o dialogo simples(simpledialog) do tkinter.
#3- Escrever o código da calculadora e usar o def.
#4- Detalhar o'que eu vou querer na minha janela.


from tkinter import *
from tkinter import simpledialog

def calculadora_interface():

    num1 = simpledialog.askinteger("Calculadora", "Digite o primeiro número:")
    num2 = simpledialog.askinteger("Calculadora", "Digite o segundo número")
    operador = simpledialog.askstring("Calculadora", "Digite o operador (+, -, *, /)")

    if operador == '+':
        resultado = num1 + num2

    elif operador == '-':

        resultado = num1-num2

    elif operador == '*':
        resultado = num1*num2

    elif operador == '/':
        resultado = num1/num2

    else:
        resultado = "Operador Inválido"

    texto_pergunta.config(text=f"O resultado é: {resultado}.")
    print(f"O resultado é: {resultado}")

janela1 = Tk()
janela1.title("Janela")
janela1.geometry("300x195")

texto_orientacao = Label(janela1, text= ("Clique no botão abaixo para ativar a calculadora."))
texto_orientacao.grid(column=0, row=0, padx=10, pady= 10)

botao = Button(janela1, text=("Clique aqui."), command=calculadora_interface)
botao.grid(column=0, row=1, padx=50, pady= 50)

texto_pergunta = Label(janela1, text="")
texto_pergunta.grid(column=0, row=2)

janela1.mainloop()


