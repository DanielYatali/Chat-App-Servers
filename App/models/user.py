from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.user_conversation import user_conversation


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique = True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_info = db.relationship('User_info', backref="user", lazy='select',  uselist = False)
    conversations = db.relationship('Conversation', secondary=user_conversation, backref='users', lazy='select')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
        }
    def toDict_info(self):
        return{
            'id': self.id,
            'username': self.username,
            'user_info': self.user_info.toDict()
        }
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

