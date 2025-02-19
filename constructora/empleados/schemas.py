from marshmallow import fields, Schema


class EmpleadoPostSchema(Schema):
    nombre = fields.String()
    puesto = fields.String()
    dpi = fields.String()
    fecha_contratacion = fields.Date()
    telefono = fields.String()
