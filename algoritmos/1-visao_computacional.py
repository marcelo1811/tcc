from my_requests import post_request, ia_url

estado_inicial = [
  ["X", "O", "O"],
  [ "_", "_", "X"],
  [ "_", "_", "O"]
]

dados_de_envio = {
  'board': estado_inicial
}

url_de_envio = ia_url

estado_final = post_request(url_de_envio, dados_de_envio)
print(estado_final)