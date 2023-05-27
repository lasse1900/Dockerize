from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write_file1', methods=['POST'])
def write_file1():
    filename = 'file1.csv'
    data = request.form['data']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Header1', 'Header2'])  # Write header line
        writer.writerow([data])  # Write user data

    return 'File 1 created and written successfully.'

@app.route('/write_file2', methods=['POST'])
def write_file2():
    filename = 'file2.csv'
    data = request.form['data']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Header1', 'Header2'])  # Write header line
        writer.writerow([data])  # Write user data

    return 'File 2 created and written successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
