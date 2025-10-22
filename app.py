from flask import  Flask, render_template, request
import tkinter as tk

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" ,creador="Said Alejandro Ramirez Chavez")




@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/carros")
def carros():
    return render_template("carros.html")

@app.route("/hacerca_de")
def hacercade():
    return render_template("hacercade.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")



@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/sesion", methods=["GET", "POST"])
def sesion():
    if request.method == "POST":
        a = request.form.get("contra1", "")
        b = request.form.get("contra2", "")
        if a == b:
            return render_template("inicio.html")
        else:
            return render_template("crearcuenta.html", error="Las contraseñas no coinciden")
    else:
        return render_template("crearcuenta.html")

if __name__ == "__main__":
    app.run(debug = True)