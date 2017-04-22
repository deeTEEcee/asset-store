from core.app import app, db
from core.models import Asset

db.create_all()
db.session.commit()
