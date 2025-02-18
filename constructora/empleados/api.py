import logging

from flask import request, Response
from flask_appbuilder.api import BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.empleados import Empleado

logger = logging.getLogger(__name__)


class EmpleadosRestApi(BaseApi):
    datamodel = SQLAInterface(Empleado)
