from flask import Flask, render_template
from counting import counting
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    # name = input("Give me your name: ")
    # print(f"The name your gave is: {name}")

    return render_template('contact.html')

# @app.route('/start_program', methods=['POST'])
# def start_program():
#     # Search Chat GPT: Filter JSON by date
#     # Perform any necessary actions or operations for your Python method/program
#     # ...

#     # Run a Python method/program using subprocess
#     # subprocess.run(['python', 'counting.py'])

#     return render_template('result.html', message='Python program started successfully.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
