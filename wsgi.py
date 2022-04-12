import click
from flask import Flask
from flask.cli import with_appcontext
from App.controllers.user_info import create_bot, create_user_info

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )


@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
@click.argument("email")
def create_user_command(username, email, password):
    create_user(username,email, password)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())

@app.cli.command("create-bots")
def create_bots():
    bots = [
            {
            "user_id": 5,
            "first_name": "daniela",
            "last_name": "Jaohn",
            "email": "daa@gmail.com",
            "country": "Tobago",
            "city": "Mayaro",
            "about": "I like to fish",
            "university": "UWI 1",
            "faculty": "Law",
            "major": "Some Law Degree",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
              {
            "user_id": 6,
            "first_name": "has",
            "last_name": "John",
            "email": "has@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "FST",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
                  {
            "user_id": 7,
            "first_name": "harry",
            "last_name": "John",
            "email": "harry@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "Med Sci",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
                  {
            "user_id": 8,
            "first_name": "Ken",
            "last_name": "John",
            "email": "ken@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "FST",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
                  {
            "user_id": 9,
            "first_name": "Hats",
            "last_name": "John",
            "email": "Hats@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "FST",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
                  {
            "user_id": 10,
            "first_name": "Helllo",
            "last_name": "John",
            "email": "helllo@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "FST",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
                  {
            "user_id": 11,
            "first_name": "tired",
            "last_name": "John",
            "email": "tired@gmail.com",
            "country": "Trinidad",
            "city": "Mayaro",
            "about": "I like to swim",
            "university": "UWI",
            "faculty": "FST",
            "major": "Computer Science",
            "movie": "Animation",
            "music": "Dance Hall",
            "photo": "link",
            "staying_in": "going out",
            "sport" : "Football",
            "bot": "bot",
            "other_info": {
                "socials":{
                    "instagram": "someaccount",
                    "twitter": "somethin1"
                }
            }
                },
        ]
        
    for bot in bots:
        # create_user(bot['first_name'], bot['email'], "pass")
        create_user_info(bot)