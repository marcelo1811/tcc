#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl
Provided as an illustration of the basic communication interface
for grbl. When grbl has finished parsing the g-code block, it will
return an 'ok' or 'error' response. When the planner buffer is full,
grbl will not send a response until the planner buffer clears space.
G02/03 arcs are special exceptions, where they inject short line 
segments directly into the planner. So there may not be a response 
from grbl for the duration of the arc.
---------------------
The MIT License (MIT)
Copyright (c) 2012 Sungeun K. Jeon
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
---------------------
"""

# Precisa instalar pyserial
# pip install pyserial
import serial
import time


def main(position):
  # Open grbl serial port
  # Port e Baud q usou no Universal GCode
  s = serial.Serial('/dev/tty.usbmodem1811',115200)

  # Wake up grbl
  s.write("\r\n\r\n".encode())
  time.sleep(2)   # Wait for grbl to initialize 
  s.flushInput()  # Flush startup text in serial input

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

  execute(position)

  # Close serial port
  s.close() 