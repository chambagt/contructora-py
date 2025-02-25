import logging

from flask import request, jsonify
from flask_appbuilder.api import expose, BaseApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from constructora.models.exc_zanja import ExcZanja, ExcZanjaPlantilla, ExcZanjaItem
from constructora.exc_zanja.schemas import ExcZanjaPlantillaPostSchema, \
    ExcZanjaPostSchema

from marshmallow import ValidationError

logger = logging.getLogger(__name__)


class ExcZanjaPlantillaRestApi(BaseApi):
    datamodel = SQLAInterface(ExcZanjaPlantilla)
    resource_name = "exczanjaplantilla"

    add_model_schema = ExcZanjaPlantillaPostSchema()

    @expose('/', methods=("POST",))
    def post(self):
        try:
            item = self.add_model_schema.load(request.json)
            data = ExcZanjaPlantilla(**item)
            self.datamodel.session.add(data)
            self.datamodel.session.commit()
            return jsonify(item), 200
        except ValidationError as error:
            return error.messages


class ExcZanjaRestApi(BaseApi):
    datamodel = SQLAInterface(ExcZanja)
    datamodelplantilla = ExcZanjaPlantillaRestApi.datamodel

    resource_name = "exczanja"

    add_model_schema = ExcZanjaPostSchema()
    add_model_plantilla_schema = ExcZanjaPlantillaRestApi.add_model_schema

    @expose('/', methods=("POST",))
    def post(self):
        try:
            item = self.add_model_schema.load(request.json)
            plantilla_id = item["exc_zanja_plantilla_id"]
            plantilla = self.datamodelplantilla.session. \
                query(ExcZanjaPlantilla). \
                filter_by(id=plantilla_id). \
                first()

            if plantilla is None:
                item_plantilla = self.add_model_plantilla_schema. \
                    load(request.json)
                data = ExcZanjaPlantilla(**item_plantilla)
                self.datamodelplantilla.session.add(data)
                self.datamodelplantilla.session.commit()
                item["exc_zanja_plantilla_id"] = data.id

            data = ExcZanja.from_dict(item)
            print(data)
            self.datamodel.session.add(data)
            self.datamodel.session.commit()
            return jsonify(item), 200
        except ValidationError as error:
            return error.messages


class ExcZanjaItemRestApi(BaseApi):
    datamodel = SQLAInterface(ExcZanjaItem)
    resource_name = "exczanjaitem"

    add_model_schema = ExcZanjaItem()
