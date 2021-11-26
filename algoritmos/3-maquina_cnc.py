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

    execute(coordenadas, count)
    print(f'movendo para {coordenadas}')
    print(f'{count}ª jogada')
    return { "coordenadas": coordenadas }

def run():
  app.run(host='0.0.0.0', port='3001')


command_list = {
  "comando_volta": "G28",
  "pos_9": "G4 P3 G0 X11.4861391021805 Y-7.34701958057155",
  "pos_8": "G4 P3 G0 X38.182066565282 Y-12.571164914159",
  "pos_7": "G4 P3 G0 X61.6718333520725 Y-18.1935207175104",
  "pos_6": "G4 P3 G0 X-10.5707293685009 Y-12.4755441667009",
  "pos_5": "G4 P3 G0 X13.3375732879919 Y-18.0921634202235",
  "pos_4": "G4 P3 G0 X37.737393952929 Y-23.6694198686948",
  "pos_3": "G4 P3 G0 X-33.1875757375047 Y-18.0045726809352",
  "pos_2": "G4 P3 G0 X-8.56780022839084 Y-23.6978561274049",
  "pos_1": "G4 P3 G0 X12.3241809829099 Y-29.3168005286991",
  "pc_1": "G4 P3 G0 X0 Y0",
  "pc_2": "G4 P3 G0 X-12.9705627484771 Y-3.27123616632825",
  "pc_3": "G4 P3 G0 X-29.6482322781408 Y-7.19960717292019",
  "pc_4": "G4 P3 G0 X-44.618795026618 Y-11.1708433392484",
  "pc_5": "G4 P3 G0 X-61.9429111656884 Y-15.0206469257085",

}

def execute(position,count):
  # comandos para cada posição do tabuleiro
  command_switcher = {
    1: (command_list["pos_1"], command_list["comando_volta"]),
    2: (command_list["pos_2"], command_list["comando_volta"]),
    3: (command_list["pos_3"], command_list["comando_volta"]),
    4: (command_list["pos_4"], command_list["comando_volta"]),
    5: (command_list["pos_5"], command_list["comando_volta"]),
    6: (command_list["pos_6"], command_list["comando_volta"]),
    7: (command_list["pos_7"], command_list["comando_volta"]),
    8: (command_list["pos_8"], command_list["comando_volta"]),
    9: (command_list["pos_9"], command_list["comando_volta"]),
  }

  commands = command_switcher.get(position, ("Inválido", "Inválido"))
  
  gCodeCommandIda = commands[0] + "\n"
  gCodeCommandVolta = commands[1] + "\n"
  gCodeCommandPeca = gcode_move_to_piece(count)

  #print("Movendo para peça...")
  # s.write('S1\n'.encode())
  turn_off_magnet()
  s.write(gCodeCommandPeca.encode()) # Envia o comando para buscar peça

#  time.sleep(20)
  #print("Fim do movimento")
  turn_on_magnet()

  #print("Movendo para jogada...")
  s.write(gCodeCommandIda.encode()) # Envia o comando de ida
 # time.sleep(5) # Esperar pelo tempo necessário para o braço chegar no destino, valor em segundos
  #print("Fim do movimento")

  turn_off_magnet()

  #print("Movendo para posição incial...")
  s.write("G4 P3\n".encode())
  s.write(gCodeCommandVolta.encode()) # Envia o comando de volta
  #print("Fim do movimento")
  # time.sleep(2) # Esperar pelo tempo necessário para o braço chegar no destino, valor em segundos

def gcode_move_to_piece(number):
  take_piece_command_name = f"pc_{number}"
  return command_list[take_piece_command_name]

def turn_on_magnet():
  #print("ligando imã...")
#  time.sleep(5)
  #s.write("S0\n".encode())
  s.write("M3\n".encode())
#  time.sleep(5)
  s.write("S1\n".encode())
  #print("imã ligado")

def turn_off_magnet():
  #print("desligando imã...")
 # time.sleep(5)
  s.write("S0\n".encode())
  s.write("M4\n".encode())
  #time.sleep(5)
  #s.write("S1\n".encode())
  #print("imã desligado")