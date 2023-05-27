from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write_csv', methods=['POST'])
def write_csv():
    filename = 'data.csv'
    data = request.form['data']

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data])

    return 'Data written successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
