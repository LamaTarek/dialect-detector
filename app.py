from flask import Flask, request, render_template
import os
import pickle

app = Flask(__name__)

# Load the model once when the app starts
model_path = r'D:/nlp project/model/SVC_model.pkl'  
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def dialect_predict(model, sentence):
    sentence = [sentence]
    dialect = model.predict(sentence)
    
    if dialect == 0:
        country = "Egypt"
    elif dialect == 1:
        country = "Lebanon"
    elif dialect == 2:
        country = "Libya"
    elif dialect == 3:
        country = "Morocco"
    else:
        country = "Sudan"
    
    return country

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    predicted_dialect = dialect_predict(model, text)
    return render_template('index.html', prediction=predicted_dialect, text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
