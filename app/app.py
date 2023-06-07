from flask import Flask, render_template,request,redirect,url_for
import sys
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length
from form import ConceptForm,EmotionCount,EmotionDescribe
# con=ConceptForm()
# con1=EmotionCount()
# con2=EmotionDescribe()


app=Flask(__name__)
app.config['SECRET_KEY']='genemo'

@app.route("/")
def step1():
    return render_template("homepage.html")

@app.route("/applyconcept")
def step2():
    inputconcept=ConceptForm(request.form)
    print(inputconcept)
    # database.save(inputconcept)
    return redirect(url_for("register",inputconcept=inputconcept))

# @app.route('/concept')
# def concept():
#     return render_template("결과창.html")


@app.route('/applyemotion', methods=['GET', 'POST'])
def register(inputconcept):
    emotioncount = EmotionCount(request.form)
    inputconcept=inputconcept
    cnt={}
    if request.method == 'POST' and emotioncount.validates():
        cnt["Happyness"]=EmotionCount.happiness.data
        cnt["Sadness"]=EmotionCount.happiness.data
        cnt["Fear"]=EmotionCount.happiness.data
        cnt["Anger"]=EmotionCount.happiness.data
        cnt["Neutral"]=EmotionCount.happiness.data
        cnt["Surprise"]=EmotionCount.happiness.data
        cnt["Disgust"]=EmotionCount.happiness.data
    
    
        return redirect(url_for('specific', cnt=cnt))
    

@app.route("/specific")
def specific(cnt):
    happiness_des={}
    sadness_des={}
    fear_des={}
    anger_des={}
    neutral_des={}
    surprise_des={}
    disgust_des={}
    emotiondescribe=EmotionDescribe(request.form)
    for i in range(cnt["Happyness"]):
        happiness_text = EmotionDescribe()
        if happiness_text.validate_on_submit():
            happiness_des[f'{i+1}'] = happiness_text.describe.data
    for i in range(cnt["Sadness"]):
        sadness_text = EmotionDescribe()
        if sadness_text.validate_on_submit():
            sadness_des[f'{i+1}'] = sadness_text.describe.data
    for i in range(cnt["Fear"]):
        fear_text = EmotionDescribe()
        if fear_text.validate_on_submit():
            fear_des[f'{i+1}'] = fear_text.describe.data
    for i in range(cnt["Anger"]):
        anger_text = EmotionDescribe()
        if anger_text.validate_on_submit():
            anger_des[f'{i+1}'] = anger_text.describe.data
    for i in range(cnt["Nutral"]):
        neutral_text = EmotionDescribe()
        if neutral_text.validate_on_submit():
            neutral_des[f'{i+1}'] = neutral_text.describe.data
    for i in range(cnt["Surprise"]):
        surprise_text = EmotionDescribe()
        if surprise_text.validate_on_submit():
            surprise_des[f'{i+1}'] = surprise_text.describe.data
    for i in range(cnt["Disgust"]):
        disgust_text = EmotionDescribe()
        if disgust_text.validate_on_submit():
            disgust_des[f'{i+1}'] = disgust_text.describe.data
    return redirect(url_for("result"))

@app.route("/result")
def step3():
    return redirect()

@app.route("/Genemo")
def Genemo():
    return redirect(url_for('step1'))


@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/contribution")
def contribution():
    return render_template("contribution.html")

@app.route("/about")
def about():
    return render_template("about.html")



# @app.route("/applyemotion")
# def applyemotion():
#     emotion1=request.args.get("inputemotion1")
#     emotion2=request.args.get("inputemotion2")
#     emotion3=request.args.get("inputemotion3")
#     emotion4=request.args.get("inputemotion4")
#     emotion5=request.args.get("inputemotion5")
#     emotion6=request.args.get("inputemotion6")
#     emotion7=request.args.get("inputemotion7")
#     print(emotion1,emotion2,emotion3,emotion4,emotion5,emotion6,emotion7)
    # database.save(emotion1,emotion2,emotion3,emotion4,emotion5,emotion6,emotion7)
    # return render_template("emotion.html")


if __name__=="__main__":
    app.run(debug=True)