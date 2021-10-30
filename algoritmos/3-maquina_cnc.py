## where code begins
# para rodar, copie e cole a linha abaixo no terminal (sem o #)
# export FLASK_APP=3-maquina_cnc.py && flask run --host 0.0.0.0 --port 3001
from minimax import findBestMove
from flask import Flask, request
import gcode

app = Flask(__name__)

@app.route('/', methods=['POST'])
def evaluate_board():
  if request.method == 'POST':
    print('--------------------------')
    print('MAQUINA CNC---------------')
    print('--------------------------')
    coordenadas = request.get_json().get('coordenadas')
    count = request.get_json().get('count')
    # gcode.main(coordenadas)
    print(f'movendo para {coordenadas}')
    print(f'{count}ª jogada')
    return { "coordenadas": coordenadas }

def run():
  app.run(host='0.0.0.0', port='3001')