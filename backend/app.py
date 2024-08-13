from flask import Flask, request, jsonify, render_template_string
import numpy as np
from tensorflow.keras.models import load_model
import os
import json

app = Flask(__name__)
model = load_model('lstm_model.keras')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Extract features from the request
        features = np.array([data['features']])

        # Convert all feature values to floats
        features = features.astype(np.float32)

        # Reshape for LSTM input
        features = features.reshape((features.shape[0], features.shape[1], 1))

        # Predict and return result
        prediction = model.predict(features)
        result = (prediction > 0.5).astype(int).tolist()

        # Save the prediction to a JSON file
        prediction_data = {
            'features': data['features'],
            'prediction': result[0][0]
        }
        
        prediction_file = 'predictions.json'

        # Load existing data if the file exists, otherwise start with an empty list
        if os.path.exists(prediction_file):
            with open(prediction_file, 'r') as f:
                predictions = json.load(f)
        else:
            predictions = []

        # Append the new prediction
        predictions.append(prediction_data)

        # Save the updated data back to the file
        with open(prediction_file, 'w') as f:
            json.dump(predictions, f, indent=4)

        return jsonify({'prediction': result[0][0]})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predictions', methods=['GET'])
def get_predictions():
    prediction_file = 'predictions.json'

    # Load existing data if the file exists
    if os.path.exists(prediction_file):
        with open(prediction_file, 'r') as f:
            predictions = json.load(f)
    else:
        predictions = []

    # Create an HTML table
    table_html = '''
    <table border="1">
        <tr>
            <th>Index</th>
            <th>Features</th>
            <th>Prediction</th>
        </tr>
        {% for i, prediction in enumerate(predictions) %}
        <tr>
            <td>{{ i + 1 }}</td>
            <td>{{ prediction['features'] }}</td>
            <td>{{ prediction['prediction'] }}</td>
        </tr>
        {% endfor %}
    </table>
    '''

    return render_template_string(table_html, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
