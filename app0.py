from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model

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
        return jsonify({'prediction': result[0][0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
