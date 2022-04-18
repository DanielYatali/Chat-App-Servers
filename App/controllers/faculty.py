from App.models import Faculty, Major
from App.database import db

def create_faculty(name):
    faculty = Faculty.query.filter_by(faculty_name = name).first()
    if faculty:
        return {"message": f"{name} already exist"}
    new_faculty = Faculty(faculty_name= name)
    db.session.add(new_faculty)
    db.session.commit()
    return {
        "message" : f"{name} created"
    }

def add_new_major(faculty_id, major_name):
    faculty = Faculty.query.get(faculty_id)
    if not faculty:
        return {"message": f"{faculty_id} does not exist"}
    major =Major.query.filter_by(major_name = major_name).first()
    if major:
        return {"message": f"{major_name} already exist"}
    new_major = Major(major_name=major_name, faculty_id=faculty_id)
    faculty.majors.append(new_major);
    db.session.commit()
    return {"message" : f"{major_name} added"}

def get_faculty_majors(faculty_id):
    faculty = Faculty.query.get(faculty_id)
    if faculty:
        majors = [major.toDict() for major in faculty.majors]
        return majors
    return{"message": f"{faculty_id} does not exist"}

def get_faculty_by_name_majors(name):
    faculty = Faculty.query.filter_by(faculty_name =  name).first()
    if faculty:
        majors = [major.toDict() for major in faculty.majors]
        return majors
    return{"message": f"{name} does not exist"}

def get_all_faculties():
    faculties = Faculty.query.all()
    if not faculties:
        return []
    
    list_faculties = [faculty.toDict() for faculty in faculties]
    return list_faculties
    
def get_all_majors():
    majors = Major.query.all()
    if not majors:
        return []
    
    list_majors = [major.toDict() for major in majors]
    return list_majors