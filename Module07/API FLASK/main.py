from flask import Flask, render_template, request , url_for
import pandas as pd
import json
app = Flask(__name__)

# @app.route(rule ,option )
@app.route('/api/health')
def health_status():
    return "Health!"

@app.route('/api/data')
def getData():
    df = pd.read_csv(r'C:\Users\conne\Documents\Orbit\Module 7\API FLASK\advertising.csv')
    return df.to_json()

@app.route('/api/predict',methods=["GET","POST"])
def predict():
    # age = request.form['email_id']
    # gender = request.form['password']
    # pred = model.predict([age,gender])
    pred = "3.4534"
    return str(pred)
    

if __name__ == "__main__":
    # app.run(host,port,debug,options)
    app.run()
