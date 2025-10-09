from flask import  Flask, render_template
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



if __name__ == "__main__":
    app.run(debug = True)