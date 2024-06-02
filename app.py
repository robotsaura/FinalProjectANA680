from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('cq4_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

