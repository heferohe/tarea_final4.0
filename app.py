from flask import Flask, request, render_template
import os
import requests, json
#from sklearn.externals import joblib
import sklearn
import joblib
from joblib import load


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        text3 = request.form['text3']
        text4 = request.form['text4']
        text5 = request.form['text5']
        text6 = request.form['text6']
        text7 = request.form['text7']
        v1=float(text1)
        v2=float(text2)
        v3=float(text3)
        v4=float(text4)
        v5=float(text5)
        v6=float(text6)
        v7=float(text7)
           
        # Aquí es donde procesarías el texto. Por ahora, solo devolvemos el mismo texto.
        source_language = ''
        #indice = text1+text2+text3+text4+text5+text6+text7
        # knn = joblib.load('modelo_entrenado.pkl') # Carga del modelo.
        # indice =knn.predict([[21.0,72.0,37.8,65.6,70.8,60.0,60.0]])
        model = load('modelv2.joblib') # Carga del modelo.
        indice2 = model.predict([[v1,v2,v3,v4,v5,v6,v7]])

        return render_template('home.html', indice=indice2,lang_detected=source_language)
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
