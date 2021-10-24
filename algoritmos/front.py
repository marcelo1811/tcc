import tkinter as tk
from threading import Thread
visao_computacional = __import__('1-visao_computacional')
ia_api = __import__('2-ia')
cnc_api = __import__('3-maquina_cnc')

thr1 = Thread(target=ia_api.run)
thr1.daemon = True
thr1.start()
thr2 = Thread(target=cnc_api.run)
thr2.daemon = True
thr2.start()

suaVez = True
count = 0
venceu = 0

def iniciar():
  global suaVez, count
  suaVez = True
  count = 0

  initiate.place_forget()
  ongoing.place(relx=0.5, rely=0.1, anchor="center")
  player.place(relx=0.5, rely=0.3, anchor="center")
  play.place(width=150, height=40, relx=0.5, rely=0.4, anchor="center")
  cancel.place(width=100, height=30, relx=0.5, rely=0.9, anchor="center")

def finalizar():
  global suaVez, count, venceu

  if suaVez == True:
    player.place_forget()
    machine.place(relx=0.5, rely=0.3, anchor="center")
    # Executa todos os processos
    venceu = visao_computacional.main()
    suaVez = False
  else:
    machine.place_forget()
    player.place(relx=0.5, rely=0.3, anchor="center")
    suaVez = True
  
  count = count + 1

  if venceu != 0:
    machine.place_forget()
    player.place_forget()
    play.place_forget()
    ongoing.place_forget()
    cancel.place_forget()
    goBack.place(width=120, height=35, relx=0.5, rely=0.9, anchor="center")

  if venceu == 1:
    resultWinner.place(relx=0.5, rely=0.2, anchor="center")
  elif venceu == 2:
    resultLoser.place(relx=0.5, rely=0.2, anchor="center")
  elif venceu == -1:
    resultNone.place(relx=0.5, rely=0.2, anchor="center")

def cancelar():
  ongoing.place_forget()
  player.place_forget()
  machine.place_forget()
  play.place_forget()
  cancel.place_forget()
  initiate.place(width=150, height=45, relx=0.5, rely=0.5, anchor="center")

def voltar():
  resultWinner.place_forget()
  resultLoser.place_forget()
  resultNone.place_forget()
  goBack.place_forget()
  initiate.place(width=150, height=45, relx=0.5, rely=0.5, anchor="center")

FONT = "Corbel"

root = tk.Tk()
root.option_add("*Font", FONT)

canvas = tk.Canvas(root, height=500, width=400, bg="white")
canvas.pack()

initiate = tk.Button(root, text="Iniciar", padx=10, pady=5, fg="black", bg="white", command=iniciar)
initiate.place(width=150, height=45, relx=0.5, rely=0.5, anchor="center")
initiate.config(font=(FONT, 20))

ongoing = tk.Label(root, text="Jogo em andamento", bg="white")
ongoing.config(font=(FONT, 28))
player = tk.Label(root, text="Sua vez", bg="white")
player.config(font=(FONT, 18))
machine = tk.Label(root, text="Vez da máquina", bg="white")
machine.config(font=(FONT, 18))

play = tk.Button(root, text="Finalizar jogada", padx=10, pady=5, fg="black", bg="white", command=finalizar)

cancel = tk.Button(root, text="Cancelar", padx=10, pady=5, fg="black", bg="white", command=cancelar)

resultWinner = tk.Label(root, text="Você ganhou", bg="white")
resultWinner.config(font=(FONT, 28))
resultLoser = tk.Label(root, text="Você perdeu", bg="white")
resultLoser.config(font=(FONT, 28))
resultNone = tk.Label(root, text="Deu velha", bg="white")
resultNone.config(font=(FONT, 28))
goBack = tk.Button(root, text="Voltar ao início", padx=10, pady=5, fg="black", bg="white", command=voltar)

root.mainloop()