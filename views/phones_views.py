from flask import Blueprint, request, jsonify, make_response
from models import Marca, Fabricante
from schemas import FabricanteSchema, MarcaSchema, EquipoSchema

phone_bp = Blueprint('phone', __name__)

@phone_bp.route("/marcas", methods=['GET'])
# @jwt_required()
def marcas():
    marcas = Marca.query.all()
    return MarcaSchema().dump(marcas, many=True)

@phone_bp.route("/fabricante", methods=['GET'])
def fabricantes():
    fabricantes = Marca.query.all()
    return FabricantesSchema().dump(fabricantes, many=True)

@phone_bp.route("/equipos-mios", methods=['GET', 'POST'])
def equipos():
    if request.method == 'POST':
        data = request.get_json()
        errors = EquipoSchema().validate(data)
        if errors:
            return make_response(jsonify(errors))
        return {}
    else:
        equipos = Marca.query.all()
        return EquipoSchema().dump(equipos, many=True)