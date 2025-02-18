from typing import Any

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Date


class Empleado(Model):
    __tablename__ = "empleado"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150))
    puesto = Column(String(100))
    dpi = Column(String(15), unique=True)
    fecha_contratacion = Column(Date)
    telefono = Column(String(15))

    @property
    def data(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "puesto": self.puesto,
            "dpi": self.dpi,
            "fecha_contratacion": self.fecha_contratacion,
            "telefono": self.telefono
        }
