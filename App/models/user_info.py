from App.database import db

class User_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_info = db.Column(db.JSON, default = {})

    def __init__(self, user_info, user_id):
        self.user_info = user_info
        self.user_id = user_id

    def toDict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'user_info': self.user_info
        }


