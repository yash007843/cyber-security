from flask import Flask, render_template, request, jsonify
import pickle
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load the trained model and vectorizer
with open('models/toxic_model.pkl', 'rb') as model_file:
    toxic_model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/try')
def try_page():
    return render_template('try.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    vectorized_text = vectorizer.transform([text])
    prediction = toxic_model.predict(vectorized_text)
    result = "Toxic" if prediction[0] == 1 else "Not Toxic"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
