from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_phone_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Fabricante, Modelo, Categoria, Caracteristica, Equipo, Stock, Proveedor, Accesorio

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/marcas", methods=['POST', 'GET'])
def marcas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()

    marcas = Marca.query.all()
    return render_template("marcas.html", marcas=marcas)
