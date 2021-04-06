from flask import Flask, render_template, request

server = Flask(__name__)


@server.route('/')
def mainpage():
    return render_template("MainPage.html")


@server.route('/CreateAccount')
def CreateAcccount():
    return render_template("CreateAccount.html")


@server.route('/SignIn')
def SignIn():
    return render_template("SignIn.html")

server.run()