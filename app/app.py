from flask import Flask, render_template,request,redirect,url_for
import sys
from form import ConceptForm,EmotionCount,EmotionDescribe


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/Genemo")
def Genemo():
    return redirect(url_for('hello'))


@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/contribution")
def contribution():
    return render_template("contribution.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/applyconcept")
def applyconcept():
    inputconcept=request.args.get("inputconcept")
    print(inputconcept)
    # database.save(inputconcept)
    return render_template("emotion.html")

@app.route("/applyemotion")
def applyemotion():
    emotion1=request.args.get("inputemotion1")
    emotion2=request.args.get("inputemotion2")
    emotion3=request.args.get("inputemotion3")
    emotion4=request.args.get("inputemotion4")
    emotion5=request.args.get("inputemotion5")
    emotion6=request.args.get("inputemotion6")
    emotion7=request.args.get("inputemotion7")
    print(emotion1,emotion2,emotion3,emotion4,emotion5,emotion6,emotion7)
    # database.save(emotion1,emotion2,emotion3,emotion4,emotion5,emotion6,emotion7)
    # return render_template("emotion.html")


if __name__=="__main__":
    app.run()