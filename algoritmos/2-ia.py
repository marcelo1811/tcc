## where code begins
# para rodar, copie e cole a linha abaixo no terminal (sem o #)
# export FLASK_APP=2-ia.py && flask run --host 0.0.0.0 --port 3000
import numpy as np
from minimax import findBestMove, isMovesLeft
from flask import Flask, request
from my_requests import post_request, maquina_cnc_url

app = Flask(__name__)

@app.route('/', methods=['POST'])
def analisar_jogo():
  if request.method == 'POST':
    print('--------------------------')
    print('IA DE ANALISE DE JOGADA---')
    print('--------------------------')
    jogo = request.get_json().get('board')
    count = request.get_json().get('count')
    bestMove, bestVal, hasMove, actualVal, nextVal = findBestMove(jogo)
  
    vencedor = 0

    print(nextVal)
    # modificado
    if not isMovesLeft(jogo):
      vencedor = -1 # Deu velha

    if nextVal == 10:
      print('Máquina venceu')
      vencedor = 2
    
    if actualVal == -10:
      print('Jogador venceu')
      vencedor = 1
    
    result = { "novo estado": jogo, "venceu": vencedor }
    print(result)

    #if hasMove and bestVal != -10:
    if hasMove and vencedor != 1:
      linha = bestMove[0]
      coluna = bestMove[1]
      jogo[linha][coluna] = "X"

      print(f'melhor jogada: {bestMove}')
      coordenadas_para_mover = encontrar_coordenadas(linha, coluna)
      dados_de_envio = {
        "coordenadas": coordenadas_para_mover,
        "count": count
      }
      post_request(maquina_cnc_url, dados_de_envio)

    return result

def encontrar_coordenadas(linha, coluna):
  if (linha == 0 and coluna == 0):
    return 1
  elif (linha == 0 and coluna == 1):
    return 2
  elif (linha == 0 and coluna == 2):
    return 3
  elif (linha == 1 and coluna == 0):
    return 4
  elif (linha == 1 and coluna == 1):
    return 5
  elif (linha == 1 and coluna == 2):
    return 6
  elif (linha == 2 and coluna == 0):
    return 7
  elif (linha == 2 and coluna == 1):
    return 8
  elif (linha == 2 and coluna == 2):
    return 9

def run():
  app.run(host='0.0.0.0', port='3000')
