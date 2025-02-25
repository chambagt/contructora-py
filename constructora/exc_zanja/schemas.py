from marshmallow import fields, Schema, EXCLUDE


class ExcZanjaPlantillaPostSchema(Schema):
    familia = fields.String()
    descripcion = fields.String()
    unidad_metrica = fields.String()
    cantidad = fields.Float()

    class Meta:
        unknown = EXCLUDE


class ExcZanjaPostSchema(Schema):
    exc_zanja_plantilla_id = fields.Integer(required=True)
    unidad_metrica = fields.String()
    cantidad = fields.Float()
    mat = fields.Float()
    mo = fields.Float()

    # Optionals
    familia = fields.String(required=False)
    descripcion = fields.String(required=False)
