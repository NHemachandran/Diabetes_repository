from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('random_forest_classification.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        Polydipsia=(request.form['Polydipsia'])
        if (Polydipsia=='Yes'):
            Polydipsia=1
        else:
            Polydipsia=0

        Weight_loss=(request.form['Weight-loss'])
        if (Weight_loss=='Yes'):
            Weight_loss=1
        else:
            Weight_loss=0

        partial_paresis=(request.form['partial-paresis'])
        if (partial_paresis=='Yes'):
            partial_paresis=1
        else:
            partial_paresis=0

        Irritability=(request.form['Irritability'])
        if (Irritability=='Yes'):
            Irritability=1
        else:
            Irritability=0

        Polyphagia=(request.form['Polyphagia'])
        if (Polyphagia=='Yes'):
            Polyphagia=1
        else:
            Polyphagia=0

        Age = int(request.form['Age'])

        visual_blurring=(request.form['visual-blurring'])
        if (visual_blurring=='Yes'):
            visual_blurring=1
        else:
            visual_blurring=0
        prediction=model.predict([[Polydipsia,Weight_loss,partial_paresis,Irritability,Polyphagia,Age,visual_blurring]])
        output=prediction[0]
        if output==0:
            return render_template('index.html',prediction_text="NEGATIVE! You don't have Diabetes")
        else:
            return render_template('index.html',prediction_text = "POSITIVE! You might have Diabetes ")
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)