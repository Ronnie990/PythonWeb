from flask import Flask,render_template
from estudiantes import Estudiantes

app = Flask(__name__)


listaestudiantes=[ 
{"matricula":1234,"foto":"imagen1.png","nombre":"Ronnie","apellido":"Ortiz","curso":"Python","estado":"aprobado"},
{"matricula":4560,"foto":"imagen2.png","nombre":"Nexido","apellido":"Rodriguez","curso":"Python","estado":"aprobado"},
{"matricula":8939,"foto":"imagen3.png","nombre":"Jorge","apellido":"Peralta","curso":"JAVA","estado":"reprobado"},
{"matricula":1020,"foto":"imagen4.png","nombre":"Raysa","apellido":"Castillo","curso":"JavaScript","estado":"aprobado"},
{"matricula":1924,"foto":"imagen5.png","nombre":"Carlos","apellido":"Tejada","curso":"JAVA","estado":"aprobado"},
{"matricula":1020,"foto":"imagen6.png","nombre":"Luis","apellido":"Gonzales","curso":"JavaScript","estado":"aprobado"},
{"matricula":1021,"foto":"imagen7.png","nombre":"Rene","apellido":"Calderon","curso":"Excell","estado":"aprobado"},
{"matricula":2034,"foto":"imagen8.png","nombre":"Pedro","apellido":"Polanco","curso":"Excell","estado":"reprobado"} 
]

@app.route("/")
def index():
    products=["Mouse","computador","television","lavadora"]
    return render_template("index.html")

@app.route("/students")
def students():
    return render_template("students.html",listaestudiantes=listaestudiantes)

@app.route("/studentdetail")
def studentdetail():
    return render_template("studentdetail.html",estudiante=listaestudiantes[0])

@app.route("/approved")
def approved():
    return render_template("approved.html",listaestudiantes=listaestudiantes)