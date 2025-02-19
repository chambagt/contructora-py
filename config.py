import os

basedir = os.path.abspath(os.path.dirname(__file__))

FAB_ADD_SECURITY_API = True
CSRF_ENABLED = True
SECRET_KEY = "secret?"

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@mysqlserver.local/quickhowto'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/constructora'
# SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_RECYCLE = 3


# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
FAB_API_SWAGGER_UI = True

UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = 1
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "Constructora"
APP_THEME = ""  # default
SESSION_TYPE = "filesystem"
# APP_INITIALIZER = 'constructora.initialization.ConstructuraAppInitializer'
