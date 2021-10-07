# export FLASK_APP=server1.py
# flask run --host 0.0.0.0 --port 5001

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sum", methods=['POST'])
def sum():
    if request.method == 'POST':
        print(request.get_json())
        print('data')
        num1 = request.get_json().get('num1')
        num2 = request.get_json().get('num2')
        print(num1)
        return {
            "result": num1 + num2
        }

def processamento_de_imagem():
    return 'imagem processada'