def validate_name(name):
    if name == "" or name == None:
        raise ValueError("Enter a valid name")

def validate_age(age):
    if age > 100 or age < 15:
        raise ValueError("Enter a valid age")

def validate_cgpa(cgpa):
    if cgpa > 10 or cgpa < 0:
        raise ValueError("Entr a valid CGPA")

def validate_skill(skill):
    if skill == "" or skill == None:
        raise ValueError("Enter a valid skill")