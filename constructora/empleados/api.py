import logging

from flask import request, Response, jsonify
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.empleados import Empleado
from constructora.empleados.schemas import EmpleadoPostSchema
from constructora.extensions import db

from marshmallow import ValidationError

logger = logging.getLogger(__name__)


class EmpleadosRestApi(BaseApi):
    datamodel = SQLAInterface(Empleado)
    resource_name = "empleados"

    add_model_schema = EmpleadoPostSchema()

    @expose('/')
    def list(self):
        empleados = self.datamodel.session.query(Empleado).all()
        empleados_json = [empleado.data for empleado in empleados]

        return jsonify(empleados_json), 200

    @expose('/', methods=("POST",))
    def post(self) -> None:
        try:
            item = self.add_model_schema.load(request.json)
            data = Empleado(**item)
            self.datamodel.session.add(data)
            self.datamodel.session.commit()
            return item
        except ValidationError as error:
            return error.messages
