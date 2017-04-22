import os
db_path = os.path.join(os.path.dirname(__file__), os.path.pardir, 'asset-store.db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
SQLALCHEMY_TRACK_MODIFICATIONS = False
