from . import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable= False)

    def __repr__(self):
        return '<Item> %r' % self.name