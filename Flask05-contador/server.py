# Flask
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "3bb8c4ef7cc83743874694003a9a111dbe3ff6d0b0f274a1c00dd72ecf8102e7"


# localhost:5000: haz que la plantilla renderice el número de veces que el 
# cliente ha visitado este sitio
@app.route("/contador")
def index():
    if "contador" not in session:
        session["contador"] = 1
    else:
        session["contador"] += 1
    return render_template("contador.html")


# localhost:5000/destroy_session: eliminar la sesión. Una vez eliminada, 
# redirige a la raíz.
@app.route("/destroy_session")
def reset():
    session.pop("contador")
    return redirect(url_for("index"))


# BONUS NINJA: agrega un botón +2 debajo del contador y una nueva ruta 
# que incremente el contador en 2
@app.route("/incrementa_en_dos")
def incrementa_en_dos():
    session["contador"] += 2
    return render_template("contador.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)