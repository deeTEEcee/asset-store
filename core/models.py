from app import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True) # not necessary if we know name is always going to be
    name = db.Column(db.String(120), unique=True)
    asset_type = db.Column(db.String(120))
    asset_class = db.Column(db.String(120))
    def __init__(self, name, asset_type, asset_class):
        self.name = name
        self.asset_type = asset_type
        self.asset_class = asset_class

    def __repr__(self):
        return '<Asset %s>' % self.name
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name' : self.name,
            'type': self.asset_type,
            'class'  : self.asset_class
        }
