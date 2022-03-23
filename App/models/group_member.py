from App.database import db

class Group_member(db.Model):
    username = db.Column(db.String, db.ForeignKey('user.username'), primary_key=True)
    conversation_name = db.Column(db.String(120), db.ForeignKey('conversation.conversation_name'), primary_key=True)
    joined_datetime = db.Column(db.String(100) ,nullable=False)


    def __init__(self, username, conversation_name, joined_datetime ):
        self.username = username
        self.conversation_name = conversation_name
        self.joined_datetime = joined_datetime

    def toDict(self):
        return{
            'username': self.username,
            'conversation_name': self.conversation_name,
            'joined_datetime': self.joined_datetime

        }
    

