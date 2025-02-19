from typing import Any

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Date


class ManoObra(Model):
    __tablename__ = "mano_obra"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(250))
    unidad = Column(Integer)
    precio = Column(Integer)

    @property
    def data(self) -> dict[str, Any]:
        return {
            "id": self.id,
        }
