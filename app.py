from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "cecytej08-aniversario"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

@app.route("/voces")
def voces():
    return render_template("voces.html")

@app.route("/orgullo")
def orgullo():
    return render_template("orgullo.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

@app.route("/futuro", methods=["GET", "POST"])
def futuro():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        grupo = request.form.get("grupo", "").strip()
        mensaje = request.form.get("mensaje", "").strip()
        if nombre and grupo and mensaje:
            flash(f"¡Gracias, {nombre}! Tu mensaje para el futuro fue recibido.", "success")
        else:
            flash("Completa los tres campos para enviar tu mensaje.", "error")
        return redirect(url_for("futuro"))
    return render_template("futuro.html")

if __name__ == "__main__":
    app.run(debug=True)
