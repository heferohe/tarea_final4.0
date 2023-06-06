from flask import Flask, request, render_template
import os
import requests, json
#import joblib



global translator_endpoint    
global cog_key    
global cog_region

try:
    cog_key = os.environ.get("COG_SERVICE_KEY")
    cog_region = os.environ.get("COG_SERVICE_REGION")      
    translator_endpoint = 'https://api.cognitive.microsofttranslator.com'   
except Exception as ex:        
    print(ex)

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
           
        # Aquí es donde procesarías el texto. Por ahora, solo devolvemos el mismo texto.
        source_language = ''
        indice = text1+text2+text3+text4+text5+text6+text7
        # knn = joblib.load('modelo_entrenado.pkl') # Carga del modelo.
        # indice =knn.predict([[21.0,72.0,37.8,65.6,70.8,60.0,60.0]])

        return render_template('home.html', indice=indice,lang_detected=source_language)
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
