from flask import Flask

app = Flask(__name__)

#Localhost:5000/: haz que diga "¡Hola Mundo!"

@app.route("/")
def index():
    return "Hola mundo!"

#numero 2
@app.route("/dojo")
def dojo():
    return "¡Dojo!"

#numero 3
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
@app.route("/say/<string:nombre>")
def say_flask(nombre):
    return f"¡Hola, {nombre.capitalize()}!"

#numero 4
@app.route('/repeat/<int:repeticiones>/<palabra>')
def repetir_palabra(repeticiones, palabra):
    resultado = palabra * repeticiones
    return resultado


if __name__ == "__main__":
    app.run(debug=True, port=5000)

