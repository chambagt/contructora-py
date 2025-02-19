import logging

from flask import request, Response
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.empleados import Empleado

logger = logging.getLogger(__name__)


class EmpleadosRestApi(BaseApi):
    datamodel = SQLAInterface(Empleado)
    resource_name = "empleados"

    @expose('/')
    def list(self):
        return "Lista de empleados"

    @expose('/', methods=("POST",))
    def post(self) -> None:
        print(request.json)

