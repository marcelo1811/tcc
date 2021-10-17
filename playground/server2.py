# export FLASK_APP=server2.py
# flask run --host 0.0.0.0 --port 5002

from flask import Flask, request
import requests

app = Flask(__name__)

# /sum?num1=1?num2=2
@app.route("/multiply", methods=['POST'])
def sum():
    if request.method == 'POST':
        print(request.get_json())
        print('data')
        multi = request.get_json().get('multi')
        num1 = request.get_json().get('num1') * multi # 1 * 3 = 3
        num2 = request.get_json().get('num2') * multi # 4 * 3 = 12

        res = requests.post(
          'http://localhost:5001/sum',
          json = {
            'num1': num1,
            'num2': num2
            'jogo-atual': [['x', 'x', 'x'], ['o', 'o', 'o']]
          }
        )
        print("resultado")
        print(res)
        return res.text