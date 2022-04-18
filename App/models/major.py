from App.database import db

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_name = db.Column(db.String(300), nullable=False)
    faculty_id =  db.Column(db.Integer, db.ForeignKey('faculty.id'))
    def __init__(self, major_name, faculty_id):
        self.major_name = major_name
        self.faculty_id = faculty_id


    def toDict(self):
        return{
            'id': self.id,
            "faculty_id": self.faculty_id,
            "faculty_name": self.faculty.faculty_name,
            "major_name": self.major_name
        }