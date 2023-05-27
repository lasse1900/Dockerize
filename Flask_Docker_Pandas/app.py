from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Load data using Pandas
    data = pd.DataFrame({'name': ['John', 'Mike', 'Sarah'],
                         'age': [25, 30, 28]})
    
    # Convert DataFrame to JSON
    json_data = data.to_json(orient='records')
    
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
