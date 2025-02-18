from constructora.extensions import (
    appbuilder,
    db,
    migrate,
    APP_DIR
)
from flask_session import Session


class ConstructuraAppInitializer:
    def __init__(self, app):
        super().__init__()

        self.constructora_app = app

    def init_view(self) -> None:
        from constructora.empleados.api import EmpleadosRestApi

        appbuilder.add_api(EmpleadosRestApi)

    def configure_middlewares(self) -> None:
        from flask_cors import CORS

        CORS(self.constructora_app)

    def setup_db(self) -> None:
        db.init_app(self.constructora_app)
        migrate.init_app(self.constructora_app, db=db, directory=APP_DIR + "/migrations")

    def configure_session(self) -> None:
        Session(self.constructora_app)

    def init_app(self) -> None:
        self.configure_session()
        self.setup_db()
        self.configure_middlewares()
        self.init_view()
