from flask import current_app, Flask

from constructora.app import create_app # noqa: F401
from constructora.extensions import (
    appbuilder, # noqa: F401
    db,  # noqa: F401
)

app: Flask = current_app
