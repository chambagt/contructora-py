from constructora.extensions import appbuilder
from constructora.empleados.api import EmpleadosRestApi


class ConstructuraAppInitializer:
    def __init__(self, app):
        super().__init__()

        self.constructora_app = app

    def init_app(self) -> None:
        appbuilder.add_api(EmpleadosRestApi)
