from App.database import db
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_name =  db.Column(db.String(120),unique=True,  nullable=False)
    private = db.Column(db.Boolean, nullable=False)
    messages = db.relationship('Message', backref = 'conversation', lazy='select')
    def __init__(self, conversation_name, private):
        self.conversation_name = conversation_name
        self.private = private

    def toDict(self):
        return{
            'conversation_id': self.id,
            'conversation_name': self.conversation_name,
            'private': self.private,
        }


    

