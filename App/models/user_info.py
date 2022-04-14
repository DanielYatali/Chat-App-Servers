from App.database import db

class User_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    photo = db.Column(db.String(300))
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    country = db.Column(db.String(120))
    city = db.Column(db.String(120))
    about = db.Column(db.String(200))
    university = db.Column(db.String(200))
    faculty = db.Column(db.String(120))
    major = db.Column(db.String(120))
    staying_in= db.Column(db.String(120))
    sport = db.Column(db.String(120))
    movie_type = db.Column(db.String(120))
    music_type = db.Column(db.String(120)) 
    bot = db.Column(db.String(120), default = "human")
    other_info = db.Column(db.JSON, default = {})

    def __init__(self, user_id, first_name, last_name, university, faculty, major, email, country, city, about, staying_in, sport, movie_type, music_type,photo,bot, other_info):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.faculty = faculty
        self.major = major
        self.email = email
        self.country = country
        self.city = city
        self.about = about
        self.staying_in = staying_in
        self.sport = sport
        self.movie_type = movie_type
        self.music_type = music_type
        self.bot = bot
        self.other_info = other_info
        self.photo = photo

    def toDict(self):
        return{
            'id': self.id,
            'username': self.user.username,
            'user_id': self.user_id,
            'photo': self.photo,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'university': self.university,
            'faculty': self.faculty,
            'major': self.major,
            'country': self.country,
            'city': self.city,
            'about': self.about,
            'staying_in': self.staying_in,
            'sport': self.sport,
            'movie': self.movie_type,
            'music': self.music_type,
            'photo': self.photo,
            'bot': self.bot,
            'other_info': self.other_info,
        }
    def chatInfo(self):
        return{
            "user_id": self.user_id,
            "username": self.user.username,
            "photo": self.photo,
            "bot": self.bot
        }


