from flask import Flask, render_template, request, session
from flask_session import Session
import datetime


app = Flask(__name__)

app.config["SESSION_PERMAMENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/")
def index():
    return "hello world"

@app.route("/starfish")
def starfish():
    return "hello starfish"

# taking user input through url
@app.route("/<string:perName>")
def general(perName):
    perName=perName.capitalize()
    return 'Hello, %s !' %perName

# rendering data from backend to be inserted into the html
@app.route("/octopus")
def octopus():
    headline="welcome and hello"
    return render_template("index.html",headName=headline)

# conditions on front end based on backend data
@app.route("/isNewYear")
def isNewYear():
    headline="welcome and hello"
    names=["Alice","Bob","Charlie"]
    now=datetime.datetime.now()
    newYear=now.month==1 and now.day==1
    return render_template("index.html",new_year=newYear,
            headName=headline,names=names)

# rerouting
@app.route("/rerouting")
def rerouting():
    return render_template("data.html")

@app.route("/more")
def more():
    return render_template("more.html")

# froms
@app.route("/forms", methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return "please submit the form"
    else:
        name=request.form.get("Name")
        return render_template("data.html", userName=name)

# session
@app.route("/session", methods=["GET","POST"])
def sessionEg():
    if session.get("notes") is None:
        session["notes"]=[]
    
    if request.method=="POST":
        note=request.form.get("note")
        session["notes"].append(note)
    return render_template("more.html", notes=session["notes"])