from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("Sensitive vs Resistant.pkl")

# Home Route (HTML Form)
@app.route('/')
def home():
    return render_template('index.html', prediction=None)

# Route for Prediction (Updating HTML Page)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [float(request.form['Q18']), float(request.form['Q8']), 
                    float(request.form['Q14']), float(request.form['Q9']), float(request.form['Q5'])]
        features = np.array([features])  # Reshape for model input
        
        # Make prediction
        prediction = model.predict(features)
        predicted_label = "Sensitive" if prediction[0] == 1 else "Resistant"

        # Render template with prediction
        return render_template('index.html', prediction=predicted_label)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
