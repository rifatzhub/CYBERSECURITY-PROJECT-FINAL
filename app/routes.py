from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/passwordcheck', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        createpassword = request.form["createpassword"]
        retypepassword = request.form["retypepassword"]
        dob = request.form["dob"].replace("/","").replace("-","")
        pet = request.form["pet"]
        location = request.form["location"]
        city = request.form["city"]
        print(createpassword)
        userquestions = model.UserquestionsAnswer(dob, pet, location, city)
        if len(userquestions) < 2:
            return render_template("questions.html", firstname = firstname, lastname = lastname, createpassword = createpassword, retypepassword = retypepassword, redirect=True) 
        recommendations = []
        if len(createpassword) < 8 or model.countUpper(createpassword) == 0 or model.countLower(createpassword) == 0 or firstname.lower() in createpassword or lastname.lower() in createpassword or model.countSymbols(createpassword) == 0 or model.countNumbers(createpassword) == 0 or (dob.lower() in createpassword and dob != "") or (pet.lower() in createpassword and pet != "") or (location.lower() in createpassword and location != "") or (city.lower() in createpassword and city != ""):
            if len(createpassword) < 12:
                recommendations.append("Please make sure your password is more than 12 characters long")
            if model.countUpper(createpassword) == 0:
                recommendations.append("Please make sure your password has more than 1 capital letter")
            if model.countLower(createpassword) == 0:
                recommendations.append("Please make sure your password has more than 1 lowercase letter")
            if firstname.lower() in createpassword:
                recommendations.append("Please make sure your password does not have your first name")
            if lastname.lower() in createpassword:
                recommendations.append("Please make sure your password does not have your last name")
            if model.countSymbols(createpassword) == 0:
                recommendations.append("Please make sure your password has more than 1 symbol")
            if model.countNumbers(createpassword) == 0:
                recommendations.append("Please make sure your password has atleast 4 numbers")
            if dob.lower() in createpassword.lower() and dob != "":
                recommendations.append("Please make sure your password does not have your date of birth")
            if pet.lower() in createpassword.lower() and pet !="":
                recommendations.append("Please make sure your password does not have your pet's name")
            if location.lower() in createpassword.lower() and location !="":
                recommendations.append("Please make sure your password does not have the city/state you were born in")
            if city.lower() in createpassword.lower() and city != "":
                recommendations.append("Please make sure your password does not have the city you currently reside in")    
            
            return render_template("weak.html", recommendations=recommendations)
        
        elif len(createpassword) in range(8,12) or model.countUpper(createpassword) == 1 or model.countLower(createpassword) == 1 or model.countSymbols(createpassword) == 1 or model.countNumbers(createpassword) in range(2,4):
            if len(createpassword) in range(8,12):
                recommendations.append("Please make sure your password is more than 12 characters long")
            if model.countUpper(createpassword) == 1:
                recommendations.append("Please make sure your password has more than 1 capital letter")
            if model.countLower(createpassword) == 1:
                recommendations.append("Please make sure your password has more than 1 lowercase letter")
            if model.countSymbols(createpassword) == 1:
                recommendations.append("Please make sure your password has more than 1 symbol")
            if model.countNumbers(createpassword) in range(2,4):
                recommendations.append("Please make sure your password has atleast 4 numbers")
            
            return render_template("ok.html", recommendations=recommendations) 
        
        else:
            return render_template("strong.html")
    else: 
        return render_template("index.html")

@app.route('/securitycheck', methods=['GET', 'POST'])
def securitycheck():
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        createpassword = request.form["createpassword"]
        retypepassword = request.form["retypepassword"]
        if createpassword != retypepassword: 
            return render_template("index.html", redirect=True)
        return render_template("questions.html", firstname = firstname, lastname = lastname, createpassword = createpassword, retypepassword = retypepassword)
    
@app.route('/forgotpassword')
def forgotpassword(): 
    return render_template('questions.1.html')