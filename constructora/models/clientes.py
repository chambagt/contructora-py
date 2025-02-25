from typing import Any

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String


class Cliente(Model):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nombre_representante = Column(String(150))
    telefono = Column(String(15))
    correo = Column(String(200), unique=True)

    @property
    def data(self) -> dict[str, Any]:
        return {
            "id": self.id,
        }
