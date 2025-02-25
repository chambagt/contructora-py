import logging

from flask import request, jsonify
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.empleados import Empleado
from constructora.empleados.schemas import EmpleadoPostSchema

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

    @expose('/<int:id>', methods=("GET",))
    def get(self, id):
        try:
            item = self.datamodel.session.query(Empleado). \
                get_or_404(id)
            return item.data
        except ValidationError as error:
            return error.messages

    @expose('/<int:id>', methods=("PUT",))
    def update(self, id):
        try:
            data_find = self.datamodel.session.query(Empleado). \
                get_or_404(id)
            item = self.add_model_schema.load(request.json, partial=True)

            for key, value in item.items():
                setattr(data_find, key, value)

            self.datamodel.session.commit()

            return data_find.data
        except ValidationError as error:
            return error.messages

    @expose('/<int:id>', methods=("DELETE",))
    def delete(self, id):
        try:
            record = self.datamodel.session.query(Empleado). \
                filter_by(id=id).delete()

            self.datamodel.session.commit()

            return { "message": record }
        except ValidationError as error:
            return error.messages
