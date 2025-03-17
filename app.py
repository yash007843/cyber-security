from flask import Flask, render_template, request, jsonify
import pickle
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Load the model and vectorizer
with open('models/toxic_model.pkl', 'rb') as model_file:
    toxic_model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to handle the text input and predict toxicity
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()  # Get the data from the POST request
        text = data['text']  # Extract the text from the request
        
        # Vectorize the text and make the prediction
        vectorized_text = vectorizer.transform([text])
        prediction = toxic_model.predict(vectorized_text)
        
        # Return the result as a JSON response
        result = "Toxic" if prediction[0] == 1 else "Not Toxic"
        return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
