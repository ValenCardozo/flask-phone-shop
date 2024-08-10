from flask import Flask, jsonify, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/flask_phone_shop'
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
            marca.is_active = 0
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

    marcas = Marca.query.filter_by(is_active=1).all()
    return render_template("marcas.html", marcas=marcas)

@app.route("/fabricantes", methods=['POST', 'GET', 'DELETE', 'PUT'])
def fabricantes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais_origen = request.form['pais_origen']
        nuevo_fabricante = Fabricante(
            nombre=nombre, 
            pais_origen=pais_origen
        )
        db.session.add(nuevo_fabricante)
        db.session.commit()

    elif request.method == 'DELETE':
        fabricante_id = request.json.get('id')
        if not fabricante_id:
            return jsonify({"error": "ID is required"}), 400

        fabricante = Fabricante.query.get(fabricante_id)
        if fabricante:
            fabricante.is_active = 0
            db.session.commit()
            return jsonify({"message": f"El fabricante se eliminó correctamente"}), 200
        else:
            return jsonify({"error": f"fabricante with ID {fabricante_id} not found"}), 404

    elif request.method == 'PUT':
        fabricante_id = request.json.get('id')
        nuevo_nombre = request.json.get('nombre')
        nuevo_pais_origen = request.json.get('paisOrigen')
        if not fabricante_id or not nuevo_nombre:
            return jsonify({"error": "ID and new name are required"}), 400

        fabricante = Fabricante.query.get(fabricante_id)
        if fabricante:
            fabricante.nombre = nuevo_nombre
            fabricante.pais_origen = nuevo_pais_origen
            db.session.commit()
            return jsonify({"message": f"fabricante with ID {fabricante_id} updated successfully"}), 200
        else:
            return jsonify({"error": f"fabricante with ID {fabricante_id} not found"}), 404

    fabricantes = Fabricante.query.filter_by(is_active=1).all()
    return render_template("fabricantes.html", fabricantes=fabricantes)

@app.route("/modelos", methods=['POST', 'GET', 'DELETE', 'PUT'])
def modelos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = Modelo(
            nombre=nombre, 
            fabricante_id=fabricante_id
        )
        db.session.add(nuevo_modelo)
        db.session.commit()

    elif request.method == 'DELETE':
        modelo_id = request.json.get('id')
        if not modelo_id:
            return jsonify({"error": "ID is required"}), 400

        modelo = Modelo.query.get(modelo_id)
        if modelo:
            modelo.is_active = 0
            db.session.commit()
            return jsonify({"message": f"El modelo se eliminó correctamente"}), 200
        else:
            return jsonify({"error": f"modelo with ID {modelo_id} not found"}), 404

    elif request.method == 'PUT':
        modelo_id = request.json.get('id')
        nuevo_nombre = request.json.get('nombre')
        nuevo_fabricante = request.json.get('fabricante_id')
        if not modelo_id or not nuevo_nombre:
            return jsonify({"error": "ID and new name are required"}), 400

        modelo = Modelo.query.get(modelo_id)
        if modelo:
            modelo.nombre = nuevo_nombre
            modelo.fabricante_id = nuevo_fabricante
            db.session.commit()
            return jsonify({"message": f"fabricante with ID {modelo.id} updated successfully"}), 200
        else:
            return jsonify({"error": f"fabricante with ID {modelo.id} not found"}), 404

    modelos = Modelo.query.filter_by(is_active=1).all()
    fabricantes = Fabricante.query.filter_by(is_active=1).all()
    return render_template("modelos.html", modelos=modelos, fabricantes=fabricantes)


