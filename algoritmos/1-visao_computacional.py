# para rodar, copie e cole a linha abaixo no terminal (sem o #)
# python 1-visao_computacional.py
from my_requests import post_request, ia_url

estado_inicial = [
  ["X", "O", "O"], # 0
  ["_", "X", "X"], # 1
  ["O", "X", "O"], # 2
] # 0 1 2

dados_de_envio = {
  'board': estado_inicial
}

url_de_envio = ia_url
print('--------------------------')
print('VISAO COMPUTACIONAL-------')
print('--------------------------')
estado_final = post_request(url_de_envio, dados_de_envio)
print(estado_final)