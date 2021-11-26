# para rodar, copie e cole a linha abaixo no terminal (sem o #)
# python 1-visao_computacional.py
from my_requests import post_request, ia_url
import visao
import json

def main(count):
#  estado_inicial = [
#    ["X", "_", "O"], # 0
#    ["_", "_", "X"], # 1
#    ["X", "_", "O"], # 2
#  ] # 0 1 2

  estado_inicial = visao.main()

  dados_de_envio = {
    'board': estado_inicial,
    'count': count
  }
  print(dados_de_envio)

  url_de_envio = ia_url
  print('--------------------------')
  print('VISAO COMPUTACIONAL-------')
  print('--------------------------')
  response = post_request(url_de_envio, dados_de_envio)
  response = json.loads(response)
  
  estado_final = response.get('novo estado')
  print(estado_final)
  vencedor = response.get('venceu')
  return vencedor

if __name__ == "__main__":
  main()