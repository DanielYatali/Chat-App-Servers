from App.database import db

user_conversation = db.Table('user_conversation',
    db.Column('id', db.Integer, primary_key = True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('conversation_id', db.Integer, db.ForeignKey('conversation.id'))    
)   