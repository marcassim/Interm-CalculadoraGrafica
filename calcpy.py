from distutils import command
from tkinter import *
from tkinter import ttk

# Cores
visor = '#1e1f1e'
co1 = '#feffff'  # branco
co2 = '#38576b'  # azul
co3 = '#ECEFF1'  # cinza
co4 = '#ff9500'  # laranja
fundo = '#3b3b3b'  # preto

# Frame Principal
janela = Tk()
janela.title('CalcPy')
janela.geometry('212x262')
janela.configure(bg=co1)

# Frame Display
frame_display = Frame(janela, width=235, height=50, bg=visor)
frame_display.grid(row=0, column=0)
# Frame Teclado
frame_teclado = Frame(janela, width=235, height=268, bg=co1)
frame_teclado.grid(row=1, column=0)

# Criando CALCULADORA


def entrar_valor(event):
    resultado = eval('9/2')

    # passar valor para o display
    valor_texto.set(resultado)


# Display
valor_texto = StringVar()
app_display = Label(frame_display, textvariable=valor_texto, width=14, height=2, padx=7,
                    relief=FLAT, anchor="e", justify=RIGHT, font=('Ive 20'), bg=visor, fg=co1)
app_display.place(x=0, y=0)

# Botões
b_1 = Button(frame_teclado, text="C", width=8, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_teclado, command=lambda: entrar_valor(), text="%", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=106, y=0)
b_3 = Button(frame_teclado, text="/", width=2, height=2, bg=co4, fg=co2,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=158, y=0)
b_4 = Button(frame_teclado, text="7", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=42)
b_5 = Button(frame_teclado, text="8", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=53, y=42)
b_6 = Button(frame_teclado, text="9", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=106, y=42)
b_7 = Button(frame_teclado, text="*", width=2, height=2, bg=co4, fg=co2,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=158, y=42)
b_8 = Button(frame_teclado, text="4", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=84)
b_9 = Button(frame_teclado, text="5", width=2, height=2, bg=co3,
             font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=53, y=84)
b_10 = Button(frame_teclado, text="6", width=2, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=106, y=84)
b_11 = Button(frame_teclado, text="-", width=2, height=2, bg=co4, fg=co2,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=158, y=84)
b_12 = Button(frame_teclado, text="3", width=2, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=126)
b_13 = Button(frame_teclado, text="2", width=2, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=53, y=126)
b_14 = Button(frame_teclado, text="1", width=2, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=106, y=126)
b_15 = Button(frame_teclado, text="+", width=2, height=2, bg=co4, fg=co2,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=158, y=126)
b_16 = Button(frame_teclado, text="0", width=8, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=168)
b_17 = Button(frame_teclado, text=".", width=2, height=2, bg=co3,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=106, y=168)
b_18 = Button(frame_teclado, text="=", width=2, height=2, bg=co4, fg=co2,
              font=('Ive 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=158, y=168)


janela.mainloop()
