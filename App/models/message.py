from App.database import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name =  db.Column(db.String(100),db.ForeignKey('user.username'),nullable=False)
    conversation_id =  db.Column(db.Integer, db.ForeignKey('conversation.id'))
    content = db.Column(db.String(300), nullable=False)
    datetime = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(300))
    def __init__(self, sender_name, conversation_id, content, datetime, photo):
        self.sender_name = sender_name
        self.conversation_id = conversation_id
        self.content = content
        self.datetime = datetime
        self.photo = photo

    def toDict(self):
        return{
            'id': self.id,
            'sender_name': self.sender_name,
            'conversation_name': self.conversation.conversation_name,
            'content': self.content,
            'datetime': self.datetime,
            "photo": self.photo
        }