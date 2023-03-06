from flask import Flask, request,  render_template
import requests


app = Flask(__name__)
@app.route('/teste')
def teste():
    return render_template('base.html')

@app.route('/gatos')
def gatoss():
    respgatos = requests.get('https://meowfacts.herokuapp.com/?count=5&lang=por')
    respPoke = respgatos.json()
    return render_template('gatos.html', respPoke=respPoke)



@app.route('/cachorros')
def cachorros():
    respimagens = requests.get('https://dogapi.dog//api/facts?number=5&lang=por')
    respNovo = respimagens.json()
    return render_template('cachorros.html',respNovo=respNovo)

@app.route('/gatosecachorros')
def gatos_e_cachorros():
    respgatos = requests.get('https://meowfacts.herokuapp.com/?count=5&lang=por')
    respPoke = respgatos.json()
    respimagens = requests.get('https://dogapi.dog//api/facts?number=5&lang=por')
    respNovo = respimagens.json()
    return render_template('gatosecachorros.html',respNovo=respNovo,respPoke=respPoke)



app.run(debug=True)