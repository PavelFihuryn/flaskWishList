from app import db


class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    url = db.Column(db.String(120), index=True)
    description = db.Column(db.Text)
    cost = db.Column(db.Integer)
    image = db.Column(db.String(128))

    def __repr__(self):
        return f'{self.id} {self.name}'
