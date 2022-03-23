from App.database import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_name =  db.Column(db.String(120),unique=True,  nullable=False)

    def __init__(self, conversation_name ):
        self.conversation_name = conversation_name

    def toDict(self):
        return{
            'id': self.id,
            'conversation_name': self.conversation_name
        }
    

