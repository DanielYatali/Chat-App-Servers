from datetime import timedelta
# SQLALCHEMY_DATABASE_URI = "sqlite:///temp-database.db"
SQLALCHEMY_DATABASE_URI = "postgresql://ybhlodepxhwwbs:75890f7ebf23b32b38ba0d8da4b2495124f1533d54e5ced84a5b15c56b7df4ef@ec2-52-203-118-49.compute-1.amazonaws.com:5432/dcrhift8i0g20l"
SECRET_KEY = "secret key"
JWT_EXPIRATION_DELTA = timedelta(days=7)
ENV = "DEVELOPMENT"