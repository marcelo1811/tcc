import requests

ia_url = 'http://localhost:3000/'

maquina_cnc_url = 'http://localhost:3001/'

def post_request(url, data):
  response = requests.post(
    url,
    json = data
  )
  return response.text


