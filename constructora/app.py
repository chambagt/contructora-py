import logging
from flask import Flask
from constructora.initialization import ConstructuraAppInitializer

logger = logging.getLogger(__name__)


def create_app():
    app = ConstructoraApp(__name__)

    try:
        app_initializer = app.config.get("APP_INITIALIZER", ConstructuraAppInitializer)(app)
        app_initializer.init_app()
        return app
    except Exception:
        logger.exception("Failed to create app")
        raise


class ConstructoraApp(Flask):
    pass
