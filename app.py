import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, request
import pickle
from flask_wtf import FlaskForm
from flask import Flask, url_for, render_template, flash, request, redirect, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_login import UserMixin
import joblib

app = Flask(__name__, static_folder='static')
svm = joblib.load("svc.pkl")
logistic = joblib.load("logistic.pkl")
naivebayes = joblib.load("naivebayes.pkl")
decisionmodel = joblib.load("decisionmodel.pkl")
scaler = joblib.load("scaler.pkl")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(UserMixin , db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    confirmpass = db.Column(db.String(80))
    email = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    contact = db.Column(db.Integer)

    def __init__(self, fullname,username, password,confirmpass,email, gender,contact):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.contact = contact
        self.confirmpass = confirmpass
        self.gender = gender

class MedicalValues(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.String(80))
    Gender = db.Column(db.String(80))
    Chestpain = db.Column(db.String(80))
    Trestbps = db.Column(db.String(80))
    Cholestrol = db.Column(db.String(80))
    Fbs = db.Column(db.String(80))
    Restecg = db.Column(db.String(80))
    Thalach = db.Column(db.String(80))
    Exang =db.Column(db.String(80))
    Oldpeak = db.Column(db.String(80))
    Slope = db.Column(db.String(80))
    Ca =db.Column(db.String(80))
    Thal =db.Column(db.String(80))

    def __init__(self,Age,Gender,Chestpain,Trestbps,Cholestrol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal):
        self.Age = Age
        self.Gender = Gender
        self.Chestpain = Chestpain
        self.Trestbps =Trestbps
        self.Cholestrol = Cholestrol
        self.Fbs = Fbs
        self.Restecg = Restecg
        self.Thalach = Thalach
        self.Exang = Exang
        self.Oldpeak = Oldpeak
        self.Slope = Slope
        self.Ca = Ca
        self.Thal = Thal


# Initialize login manager
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))



@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('homepage.html')
    else:
        if request.method == 'POST':
            return render_template('homepage.html')
        return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                user_object = User.query.filter_by(username=name).first()
                login_user(user_object)
                return redirect(url_for('predict'))
            else:
                return render_template('login.html', msg="Invalid Login Details")
        except:
            return render_template('login.html', msg="Invalid Login")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'],
                        fullname=request.form['fullname'],email=request.form['email'], contact=request.form['contact'],
                        confirmpass = request.form['confirmpass'],gender=request.form['gender']
                        )
        userr = request.form['username']
        result = User.query.filter_by(username=userr).first()

        passw = request.form['password']
        confpass = request.form['confirmpass']

        if passw != confpass:
            return render_template('register.html', msg="Please Enter the Same Password")

        if userr == passw:
            return render_template('register.html', msg="Username and Password Should not be same")

        if result is None:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', msg="Username already exists")

    return render_template('register.html')


@app.route('/predict/', methods=['POST', 'GET'])
def predict():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:

        if request.method == "POST":


            new_data = MedicalValues(Age=request.form.get("Age"), Gender=request.form.get("Gender"),
                        Chestpain= request.form.get("Cp"),Trestbps=request.form.get("Trestbps"), Cholestrol=request.form.get("Chol"),
                        Fbs = request.form.get("Fbs"),Restecg=request.form.get("Restecg"),Thalach=request.form.get("Thalach"),Exang=request.form.get("Exang"),
                        Oldpeak=request.form.get("Oldpeak"),Slope=request.form.get("Slope"),Ca=request.form.get("Ca"),Thal=request.form.get("Thal"))
            
            db.session.add(new_data)
            db.session.commit()

                        
            age = request.form.get("Age")
            gender = request.form.get("Gender")
            chestpain = request.form.get("Cp")
            trestbps = request.form.get("Trestbps")
            chol = request.form.get("Chol")
            fbs = request.form.get("Fbs")
            restecg = request.form.get("Restecg")
            thalach = request.form.get("Thalach")
            exang = request.form.get("Exang")
            oldpeak = request.form.get("Oldpeak")
            slope = request.form.get("Slope")
            ca = request.form.get("Ca")
            thal = request.form.get("Thal")
            return redirect(
                url_for('predicted', age=age, gender=gender, chestpain=chestpain, trestbps=trestbps, chol=chol, fbs=fbs,
                    restecg=restecg,
                    thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal))
        else:
            return render_template('index.html')


@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/predicted/')
def predicted():
    age = request.args.get('age', None)
    gender = request.args.get('gender', None)
    chestpain = request.args.get('chestpain', None)
    trestbps = request.args.get('trestbps', None)
    chol = request.args.get('chol', None)
    fbs = request.args.get('fbs', None)
    restecg = request.args.get('restecg', None)
    thalach = request.args.get('thalach', None)
    exang = request.args.get('exang', None)
    oldpeak = request.args.get('oldpeak', None)
    slope = request.args.get('slope', None)
    ca = request.args.get('ca', None)
    thal = request.args.get('thal', None)

    input_features = []
    input_features.append(age)
    input_features.append(gender)
    input_features.append(chestpain)
    input_features.append(trestbps)
    input_features.append(chol)
    input_features.append(fbs)
    input_features.append(restecg)
    input_features.append(thalach)
    input_features.append(exang)
    input_features.append(oldpeak)
    input_features.append(slope)
    input_features.append(ca)
    input_features.append(thal)

    # scaler_array = []
    # scaler_array.append(age)
    # scaler_array.append(trestbps)
    # scaler_array.append(chol)
    # scaler_array.append(thalach)
    # scaler_array.append(oldpeak)
    #
    input_features = [[age, gender, chestpain, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

    # scaler_array = []
    # scaler_array.append(age)
    # scaler_array.append(trestbps)
    # scaler_array.append(chol)
    # scaler_array.append(thalach)
    # scaler_array.append(oldpeak)
    #

    scaler_array = scaler.transform(input_features)

    features_name = ["Age", "Gender", "Cp", "Trestbps", "Chol", "Fbs", "Restecg", "Thalach", "Exang", "Oldpeak",
                     "Slope", "Ca", "Thal"]

    df = pd.DataFrame(scaler_array, columns=features_name)

    output1 = int(svm.predict(df))
    output2 = int(logistic.predict(df))
    output3 = int(naivebayes.predict(df))
    output4 = int(decisionmodel.predict(df))

    print(output1, output2, output3, output4)

    output = output1 + output2 + output3 + output4

    if output1 == 1:
        output1 = "1"
    else:
        output1 = "0"

    if output2 == 1:
        output2 = "1"
    else:
        output2 = "0"

    if output3 == 1:
        output3 = "1"
    else:
        output3 = "0"

    if output4 == 1:
        output4 = "1"
    else:
        output4 = "0"

    if output >= 2:
        return render_template('result.html', resmsg='You have a Risk of Heart Disease', op1=output1, op2=output2,
                               op3=output3, op4=output4)
    else:
        return render_template('result.html', resmsg='You have No Risk of Heart Disease', op1=output1, op2=output2,
                               op3=output3, op4=output4)



if __name__ == "__main__":
    db.create_all()
    app.secret_key = "123"
    app.run(debug=True)
