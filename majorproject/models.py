from majorproject import db
from datetime import datetime

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    thana_code = db.Column(db.String(20), nullable=False)
    parent_name = db.Column(db.String(20), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Child %r>' % self.name