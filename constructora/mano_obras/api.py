import logging

from flask import request, Response
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.mano_obras import ManoObra

logger = logging.getLogger(__name__)


class ManoObrasRestApi(BaseApi):
    datamodel = SQLAInterface(ManoObra)
    resource_name = "manoobras"

    @expose('/')
    def list(self):
        return "Lista de manoobras"

