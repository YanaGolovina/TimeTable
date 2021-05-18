from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    userType = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.id


@app.route('/')
@app.route('/MainPage')
def mainpage():
    return render_template("MainPage.html")


@app.route('/CreateAccount', methods=['POST', 'GET'])
def CreateAcccount():
    if request.method == "POST":
        firstName = request.form['firstName']
        name = request.form['name']
        group = request.form['group']
        email = request.form['email']
        password = request.form['pass']
        userType = request.form['userType']
        user = Users(firstName=firstName, name=name, group=group, email=email, password=password, userType=userType)
        db.session.add(user)
        db.session.commit()
        return render_template("MainPage.html")
    else:
        users = Users.query.order_by(Users.id).all()
        return render_template("CreateAccount.html", users=users)


@app.route('/SignIn')
def SignIn():
    return render_template("SignIn.html")

if __name__ == "__main__":
    app.run(debug=True)