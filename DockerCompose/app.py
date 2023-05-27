from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return f"Counter: {session['counter']}"

@app.route('/reset')
def reset():
    session.pop('counter', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
