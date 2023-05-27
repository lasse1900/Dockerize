from flask import Flask
from counting import counting

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/start')
def start():
    counting()
    return "Start"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
