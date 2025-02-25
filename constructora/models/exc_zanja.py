"""
Este modelo hace referencia a las hojas de excel
en el documento inicial.
ExcZanja corresponde a "MT EXC ZANJA"
"""

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class ExcZanjaPlantilla(Model):
    __tablename__ = "exc_zanja_plantilla"
    id = Column(Integer, primary_key=True)
    familia = Column(String(15))
    descripcion = Column(String)
    unidad_metrica = Column(String(5))
    cantidad = Column(Float(3))


class ExcZanja(Model):
    __tablename__ = "exc_zanja"
    id = Column(Integer, primary_key=True)
    exc_zanja_plantilla_id = Column(Integer, ForeignKey('exc_zanja_plantilla.id'), nullable=False)
    exc_zanja_plantilla = relationship("ExcZanjaPlantilla")
    unidad_metrica = Column(String(5))
    cantidad = Column(Float(3))
    mat = Column(Float(3))
    mo = Column(Float(3))

    @classmethod
    def from_dict(cls, data):
        valid_fields = {
            column.name for column in cls.__table__.columns
        }

        filtered_data = {
            key: value for key, value in data.items() if key in valid_fields
        }

        return cls(**filtered_data)


class ExcZanjaItem(Model):
    __tablename__ = "exc_zanja_item"
    id = Column(Integer, primary_key=True)
    exc_zanja_id = Column(Integer, ForeignKey('exc_zanja.id'), nullable=False)
    exc_zanja = relationship("ExcZanja")
    codigo = Column(String(15))
    nombre = Column(String(15))
    descripcion = Column(String)
    rendimiento_hora = Column(Float(3))
    dist = Column(Float(3))
    dist_hora = Column(Float(3))
    valor_hora = Column(Float(3))
    valor_galon = Column(Float(3))
    valor_dist = Column(Float(3))
    factor = Column(Float(3))
