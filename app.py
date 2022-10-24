from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {
    'Mike': 'Chatlotte Hack',
    'John': 'Code 9',
    'Sam': 'Women Who Code',
    'Tim': 'Runtime Terror',
    'Brett': 'Frontpage Freebirds'
    }

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    

    currentDate = datetime.datetime.now()

    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')
    


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    global message
    number = request.form['number']
    message = 'not an integer.'

    # Write your to code here to check whether number is even or odd and render result.html page
    if number == None or number =="":
        message = "Nothing Was Entered"
    elif int(number) %2 == 0:
        message = 'is Even.'
    elif int(number)%2 ==0:
        message = "is Odd."
    return render_template('result.html', number=number, message=message)

    
@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['org']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = studentOrg

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)