from flask import Flask, render_template, jsonify
from my_module import my_method

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_csv')
def start_method():
    result = my_method()
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
