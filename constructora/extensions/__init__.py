import os

from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate

APP_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
db = SQLA()
migrate = Migrate()
appbuilder = AppBuilder(db.session)
