## where code begins
# para rodar, copie e cole a linha abaixo no terminal (sem o #)
# export FLASK_APP=3-maquina_cnc.py && flask run --host 0.0.0.0 --port 3001
from flask import Flask, request
import serial
import time
import gcode

# Open grbl serial port
# Port e Baud q usou no Universal GCode
s = serial.Serial('COM3',115200)

# Wake up grbl
s.write("\r\n\r\n".encode())
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

app = Flask(__name__)

@app.route('/', methods=['POST'])
def evaluate_board():
  if request.method == 'POST':
    print('--------------------------')
    print('MAQUINA CNC---------------')
    print('--------------------------')
    coordenadas = request.get_json().get('coordenadas')
    count = request.get_json().get('count')
    # execute(coordenadas)
    print(f'movendo para {coordenadas}')
    print(f'{count}ª jogada')
    return { "coordenadas": coordenadas }

def run():
  app.run(host='0.0.0.0', port='3001')

def execute(position):
  # comandos para cada posição do tabuleiro
  command_switcher = {
    1: ("comando_ida", "comando_volta"),
    2: ("comando_ida", "comando_volta"),
    3: ("comando_ida", "comando_volta"),
    4: ("comando_ida", "comando_volta"),
    5: ("comando_ida", "comando_volta"),
    6: ("comando_ida", "comando_volta"),
    7: ("comando_ida", "comando_volta"),
    8: ("comando_ida", "comando_volta"),
    9: ("comando_ida", "comando_volta"),
  }

  commands = command_switcher.get(position, ("Inválido", "Inválido"))
  gCodeCommandIda = commands[0] + "\n"
  gCodeCommandVolta = commands[1] + "\n"

  s.write(gCodeCommandIda.encode()) # Envia o comando de ida
  # time.sleep(2) # Esperar pelo tempo necessário para o braço chegar no destino, valor em segundos
  s.write(gCodeCommandVolta.encode()) # Envia o comando de volta
  # time.sleep(2) # Esperar pelo tempo necessário para o braço chegar no destino, valor em segundos