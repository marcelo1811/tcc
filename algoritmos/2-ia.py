## where code begins
# export FLASK_APP=2-ia.py && flask run --host 0.0.0.0 --port 3001
import numpy as np
from minimax import findBestMove
from flask import Flask, request
from my_requests import post_request, maquina_cnc_url

app = Flask(__name__)

@app.route('/', methods=['POST'])
def evaluate_jogo():
  if request.method == 'POST':
    jogo = request.get_json().get('board')
    bestMove, bestVal = findBestMove(jogo)

    linha = bestMove[0]
    coluna = bestMove[1]
    jogo[linha][coluna] = "O"
    
    dados_de_envio = {
      "coordenadas": {
        "x": 1,
        "y": 2,
      }
    }
    post_request(maquina_cnc_url, dados_de_envio)
    
    result = { "melhor jogada": jogo }
    print(result)
    return result