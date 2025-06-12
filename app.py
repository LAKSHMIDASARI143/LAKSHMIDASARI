
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('crop_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/recommendation', methods=['POST'])
def recommend():
    try:
        data = request.form
        features = [
            float(data['nitrogen']),
            float(data['phosphorus']),
            float(data['potassium']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]
        prediction = model.predict([features])
        return f"Recommended Crop: <b>{prediction[0]}</b>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
