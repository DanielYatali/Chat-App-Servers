from App.database import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name =  db.Column(db.String(100),db.ForeignKey('user.username'),nullable=False)
    conversation_name =  db.Column(db.String(100), db.ForeignKey('conversation.conversation_name'), nullable=False )
    content = db.Column(db.String(300), nullable=False)
    datetime = db.Column(db.String(100), nullable=False)
    def __init__(self, sender_name, conversation_name, content, datetime):
        self.sender_name = sender_name
        self.conversation_name = conversation_name
        self.content = content
        self.datetime = datetime

    def toDict(self):
        return{
            'id': self.id,
            'sender_name': self.sender_name,
            'conversation_name': self.conversation_name,
            'content': self.content,
            'datetime': self.datetime
        }