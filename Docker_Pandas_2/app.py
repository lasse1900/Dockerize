from flask import Flask, render_template, request
import time
# from flask import Flask
name = ""

app = Flask(__name__)

def greet(name):
    print("Test")
    counting()
    return f"Hello, {name}!"

def counting():
    for i in range(5):
        print(i)
        time.sleep(1)
    print("I have reached the END !!")
    # return render_template('contact.html')


print(greet('Tom Jones'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
