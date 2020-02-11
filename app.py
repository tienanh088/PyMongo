from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://FlaskMongoDB:flask1234@mongodb-hpxzi.mongodb.net/PyMongo"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/add', methods=['POST', 'GET'])
def add_student():
    try:
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        address = request.form.get('address')
        city = request.form.get('city')
        gender = request.form.get('gender')
        pin = request.form.get('pin')

        mongo.db.students.insert_one({'firstname' : firstname, 'lastname' : lastname, 'address' : address, 'city' : city, 'gender' : gender, 'pin' : pin})
        msg = 'Record successfully added'
    except:
        msg = 'Error in insert operation'
    finally:
        return render_template('result.html', msg = msg)

@app.route('/list')
def list():
    student = mongo.db.students.find()
    return render_template('list.html', students = student)