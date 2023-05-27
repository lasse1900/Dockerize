from flask import Flask

subapp = Flask(__name__)

@subapp.route('/sub')
def sub():
    return "Hello, Sub-App!"

if __name__ == '__main__':
    subapp.run(debug=True, host='0.0.0.0')
