from app import ma
from models import User, Fabricante, Marca, Equipo, Modelo, Categoria
from marshmallow import validates, ValidationError

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    is_admin = ma.auto_field()

class MinimalUserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()

class FabricanteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Fabricante

    nombre = ma.auto_field()
    pais_origen = ma.auto_field()

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca

    nombre = ma.auto_field()

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    nombre = ma.auto_field()

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    nombre = ma.auto_field()
    fabricante = ma.Nested(FabricanteSchema)

class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo

    nombre = ma.auto_field()
    costo = ma.auto_field()
    modelo = ma.auto_field()

    @validates('costo')
    def validate_costo(self, value):
        if value > 100000:
            raise ValidationError('El costo es altisimo')
    # categoria = ma.Nested(CategoriaSchema)