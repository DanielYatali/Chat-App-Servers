from datetime import timedelta
SQLALCHEMY_DATABASE_URI = "sqlite:///temp-database.db"
SECRET_KEY = "SECRET"
JWT_EXPIRATION_DELTA = timedelta(days=7)
# ENV = "DEVELOPMENT"
ENV = "PRODUCTION"