import logging

from flask import request, Response
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.clientes import Cliente

logger = logging.getLogger(__name__)


class ClientesRestApi(BaseApi):
    datamodel = SQLAInterface(Cliente)
    resource_name = "cliente"

    @expose('/')
    def list(self):
        return "Lista de clientes"
