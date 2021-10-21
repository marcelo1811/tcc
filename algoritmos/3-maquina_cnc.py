## where code begins
# export FLASK_APP=3-maquina_cnc.py && flask run --host 0.0.0.0 --port 3001
from minimax import findBestMove
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def evaluate_board():
  if request.method == 'POST':
    coordenadas = request.get_json().get('coordenadas')
    print(f'movendo para {coordenadas}')
    return { "coordenadas": coordenadas }