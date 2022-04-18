import json
import click
from App.controllers.conversation import create_conversation
from App.controllers.user_info import create_bot
from App.controllers.faculty import create_faculty, add_new_major
# from App.controllers.user_info import create_bot, create_user_info

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
    with open('./dummy_data/bots.json') as json_file:
        bots = json.load(json_file)
        i = 0
        for bot in bots:
            print(create_user(bot["first_name"] + "_" + bot["last_name"]+ f"{i}", bot["email"], bot["first_name"]+"pass"))
            print(create_bot(bot))
            i += 1

@app.cli.command("create-groups")
def create_groups():
     with open('./dummy_data/groups.json') as json_file:
        groups = json.load(json_file)
        for group in groups:
            print(create_conversation(group["conversation_name"], group["private"], group["photo"], group["criteria"]))

@app.cli.command("create-faculty-data")
def create_faculty_data():
     with open('./dummy_data/faculty_data.json') as json_file:
        faculties = json.load(json_file)
        i = 1
        for faculty in faculties:
            print(create_faculty(faculty))
            for major in faculties[faculty]:
                print(add_new_major(i,major ))
            i += 1