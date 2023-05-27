from flask import Flask, render_template, request

app = Flask(__name__)

diary_entries = []

@app.route('/')
def home():
    return render_template('index.html', entries=diary_entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = request.form['entry']
    diary_entries.append(entry)
    return render_template('index.html', entries=diary_entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
