def checkPassword(createpassword,retypepassword, firstname,lastname):
        if createpassword != retypepassword:
            return "try again"
        elif firstname.lower() in createpassword.lower() or lastname.lower() in createpassword:
            return "weak password"
        elif len(createpassword) < 8:
            return "weak password"
        elif len(createpassword) == range(9,12):
            return "ok password"
        elif len(createpassword) > 12:
            return "strong password"
        # elif #Capital:
        # elif #Lowercase:
        elif (any(c.islower() for c in createpassword)):
            return
        # elif #Numbers:
        # elif #Symbols:
        else:
            return "strong password"

def countUpper(createpassword): 
    count = 0
    for c in createpassword: 
        if c.isupper(): 
            count += 1
    return count 
    
def countLower(createpassword): 
    count = 0
    for c in createpassword: 
        if c.islower(): 
            count += 1
    return count
    
def countSymbols(createpassword): 
    count = 0
    for c in createpassword: 
        if not (c.isalpha() or c.isnumeric()): 
            count += 1
    return count
    
def countNumbers(createpassword): 
    count = 0
    for c in createpassword: 
        if not c.isnumeric(): 
            count += 1
    return count

def UserquestionsAnswer(dob, pet, location, city):
    answers = []
    if dob != "":
        answers.append(dob)
    if pet != "":
        answers.append(pet)
    if location != "":
        answers.append(location)
    if city != "":
        answers.append(city)
    return answers    