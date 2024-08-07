from flask import Flask, jsonify, render_template, redirect, request
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

@app.route("/marcas", methods=['POST', 'GET', 'DELETE', 'PUT'])
def marcas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()

    elif request.method == 'DELETE':
        marca_id = request.json.get('id')
        if not marca_id:
            return jsonify({"error": "ID is required"}), 400

        marca = Marca.query.get(marca_id)
        print(marca)
        if marca:
            db.session.delete(marca)
            db.session.commit()
            return jsonify({"message": f"La marca se eliminó correctamente"}), 200
        else:
            return jsonify({"error": f"Marca with ID {marca_id} not found"}), 404

    elif request.method == 'PUT':
        marca_id = request.json.get('id')
        nuevo_nombre = request.json.get('nombre')
        if not marca_id or not nuevo_nombre:
            return jsonify({"error": "ID and new name are required"}), 400

        marca = Marca.query.get(marca_id)
        if marca:
            marca.nombre = nuevo_nombre
            db.session.commit()
            return jsonify({"message": f"Marca with ID {marca_id} updated successfully"}), 200
        else:
            return jsonify({"error": f"Marca with ID {marca_id} not found"}), 404

    marcas = Marca.query.all()
    return render_template("marcas.html", marcas=marcas)
