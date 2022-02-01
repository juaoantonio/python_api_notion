from tkinter import *


def print_day(msg):
    print(msg)


dia_semana = [
    'Segunda-Feira',
    'Terça-Feira',
    'Quarta-Feira',
    'Quinta-Feira',
    'Sexta-Feira',
    'Sábado',
]

root = Tk()
root.title("Selecionar")

# dimensões da janela
largura = 400
altura = 400

# Resolução do nosso sistema
largura_display = root.winfo_screenwidth()
altura_display = root.winfo_screenheight()

# posição da janela
posx = int((largura_display / 2) - (largura / 2))
posy = int((altura_display / 2) - (altura / 2))

root.geometry(f"{largura}x{altura}+{posx}+{posy}")

root.resizable(False, False)

# Botão
# btn = Button(root, text='Mensagem', command=lambda: print_msg('Olá'))
# btn.pack()

root.mainloop()
