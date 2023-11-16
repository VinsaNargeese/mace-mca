from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__)

# Load your trained model
model = joblib.load("RFC_model.pkl") # Replace with the path to your model file
scalar = pickle.load(open('credit_card.pkl', 'rb'))
@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        data = [
            float(request.form['V1']),
            float(request.form['V2']),
            float(request.form['V3']),
            float(request.form['V4']),
            float(request.form['V5']),
            float(request.form['V6']),
            float(request.form['V7']),
            float(request.form['V8']),
            float(request.form['V9']),
            float(request.form['V10']),
            float(request.form['V11']),
            float(request.form['V12']),
            float(request.form['V13']),
            float(request.form['V14']),
            float(request.form['V15']),
            float(request.form['V16']),
            float(request.form['V17']),
            float(request.form['V18']),
            float(request.form['V19']),
            float(request.form['V20']),
            float(request.form['V21']),
            float(request.form['V22']),
            float(request.form['V23']),
            float(request.form['V24']),
            float(request.form['V25']),
            float(request.form['V26']),
            float(request.form['V27']),
            float(request.form['V28']),
            float(request.form['Amount'])  # Get the 'Amount' input field
        ]
        print(data)
        #scaled_features = scalar.transform([data])
        #print(scaled_features)
        #res=[[-5.1925,3.164721,-5.04768,2.246597,-4.01178,-0.63891,-2.87346,1.576318,-2.86199,-2.12046,1.863596,-3.620251763,-1.480714422,-1.583343405,-1.230469222,-1.20229797,-6.167636538,-2.651539049,0.013587706,-1.850469964,1.167243794,-1.006617493,0.774561804,0.063396917,-0.390657771,1.884740675,-1.742557515,-0.082215935,247.86]]
        # Make a prediction using the loaded model
        prediction = model.predict([data])
        print(prediction)
        if prediction== 0:
            result = "Normal Transaction"   
        else:
            result = "Fraudulent Transaction"

        return render_template('result.html', result=result)
    except Exception as e:
        return render_template('result.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
