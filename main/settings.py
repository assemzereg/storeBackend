import os

class Settings:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROJECT_HOME = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(PROJECT_HOME, 'static', 'uploads')


class DevSettings(Settings):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:toor@localhost:5432/Store'


class ProdSettings(Settings):
    SQLALCHEMY_DATABASE_URI=''