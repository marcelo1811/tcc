import tkinter as tk
import time
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
  ongoing.place(relx=0.4, rely=0.1)
  player.place(relx=0.4, rely=0.2)
  play.place(width=100, height=30, relx=0.4, rely=0.3)
  cancel.place(width=100, height=30, relx=0.4, rely=0.9)

def finalizar():
  global suaVez, count, venceu

  if suaVez == True:
    player.place_forget()
    machine.place(relx=0.4, rely=0.2)
    # Executa todos os processos
    venceu = visao_computacional.main()
    suaVez = False
  else:
    machine.place_forget()
    player.place(relx=0.4, rely=0.2)
    suaVez = True
  
  count = count + 1

  if venceu != 0:
    machine.place_forget()
    player.place_forget()
    play.place_forget()
    ongoing.place_forget()
    cancel.place_forget()
    goBack.place(width=100, height=30, relx=0.4, rely=0.9)

  if venceu == 1:
    resultWinner.place(relx=0.4, rely=0.2)
  elif venceu == 2:
    resultLoser.place(relx=0.4, rely=0.2)
  elif venceu == -1:
    resultNone.place(relx=0.4, rely=0.2)

def cancelar():
  ongoing.place_forget()
  player.place_forget()
  machine.place_forget()
  play.place_forget()
  cancel.place_forget()
  initiate.place(width=100, height=30, relx=0.4, rely=0.1)

def voltar():
  resultWinner.place_forget()
  resultLoser.place_forget()
  resultNone.place_forget()
  goBack.place_forget()
  initiate.place(width=100, height=30, relx=0.4, rely=0.1)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=400, bg="white")
canvas.pack()

initiate = tk.Button(root, text="Iniciar", padx=10, pady=5, fg="black", bg="white", command=iniciar)
initiate.place(width=100, height=30, relx=0.4, rely=0.1)

ongoing = tk.Label(root, text="Jogo em andamento", bg="white")
player = tk.Label(root, text="Sua vez", bg="white")
machine = tk.Label(root, text="Vez da máquina", bg="white")

play = tk.Button(root, text="Finalizar jogada", padx=10, pady=5, fg="black", bg="white", command=finalizar)

cancel = tk.Button(root, text="Cancelar", padx=10, pady=5, fg="black", bg="white", command=cancelar)

resultWinner = tk.Label(root, text="Você ganhou", bg="white")
resultLoser = tk.Label(root, text="Você perdeu", bg="white")
resultNone = tk.Label(root, text="Deu velha", bg="white")
goBack = tk.Button(root, text="Voltar ao início", padx=10, pady=5, fg="black", bg="white", command=voltar)

root.mainloop()