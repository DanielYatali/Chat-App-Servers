from App.database import db

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(300), nullable=False)
    majors = db.relationship('Major', backref = 'faculty', lazy='select')
    def __init__(self, faculty_name):
        self.faculty_name = faculty_name

    def toDict(self):
        return{
            'id': self.id,
            "faculty_name": self.faculty_name
        }