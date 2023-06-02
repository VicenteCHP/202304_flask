"""Tablero de ajedrez."""

# Flask
from flask import Flask, render_template

app = Flask(__name__)

# 1. localhost:5000: debería mostrar un tablero de ajedrez de 8 por 8
@app.route("/")
def tablero_uno():
    return render_template(
        "tablero_de_ajedrez.html",
        fila=8,
        columna=8,
        color_uno="red",
        color_dos="black",
    )

# 2. localhost:5000/4: debería mostrar un tablero de ajedrez de 8 (columnas) por 4 (filas)
@app.route("/<int:fila>")
def tablero_dos(fila):
    return render_template(
        "tablero_de_ajedrez.html",
        fila=fila,
        columna=8,
        color_uno="red",
        color_dos="black",
    )

# 3. localhost:5000/(x)/(y): debería mostrar un tablero de ajedrez de x por y
# Por ejemplo, localhost:5000/10/10 debería mostrar un tablero de ajedrez de 10 por 10. 
# Antes de pasar x y a Jinja, recuerda primero convertirlos a enteros (para que puedas usar x o y en un bucle for)
@app.route("/<int:columna>/<int:fila>")
def tablero_tres(columna, fila):
    return render_template(
        "tablero_de_ajedrez.html",
        fila=fila,
        columna=columna,
        color_uno="red",
        color_dos="black",
    )

# BONUS SENSEI: Haz que otra ruta acepte 4 parámetro (es decir, "/<x>/<y>/<color1>/<color2>") y 
# renderiza un tablero de ajedrez con x filas e y columnas, con colores alternos, color1 y color2
@app.route("/<int:columna>/<int:fila>/<string:color_uno>/<string:color_dos>")
def tablero_bonus(columna, fila, color_uno, color_dos):
    return render_template(
        "tablero_de_ajedrez.html",
        fila=fila,
        columna=columna,
        color_uno=color_uno,
        color_dos=color_dos,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
