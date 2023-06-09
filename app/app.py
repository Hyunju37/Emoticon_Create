from flask import Flask, render_template, redirect, url_for, session,request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, ValidationError

import os

# 파일 저장 함수
def save_data_to_file(data):
    filename = 'data.txt'
    with open(filename, 'a') as file:
        file.write(data + '\n')

class ConceptForm(FlaskForm):
    concept = StringField('개념', validators=[InputRequired()])

class PersonalizeStatus(FlaskForm):
    status = SelectField('개인화 상태', choices=[('yes', '예'), ('no', '아니오')])

class EmotionCount(FlaskForm):
    happiness = IntegerField('Happiness', validators=[NumberRange(min=0, max=32)])
    sadness = IntegerField('Sadness', validators=[NumberRange(min=0, max=32)])
    anger = IntegerField('Anger', validators=[NumberRange(min=0, max=32)])
    disgust = IntegerField('Disgust', validators=[NumberRange(min=0, max=32)])
    neutral = IntegerField('Neutral', validators=[NumberRange(min=0, max=32)])
    surprise = IntegerField('Surprise', validators=[NumberRange(min=0, max=32)])
    fear = IntegerField('Fear', validators=[NumberRange(min=0, max=32)])

    def validate(self, extra_validators=None):
        if not super().validate(extra_validators):
            return False
        total = (
            self.happiness.data + self.sadness.data + self.anger.data +
            self.disgust.data + self.neutral.data + self.surprise.data +
            self.fear.data
        )
        if total != 32:
            raise ValidationError('감정 개수의 합은 반드시 32여야 합니다.')
        return True

class EmotionDescribe(FlaskForm):
    happiness_description = TextAreaField('기쁨 감정 설명', validators=[InputRequired()])
    sadness_description = TextAreaField('슬픔 감정 설명', validators=[InputRequired()])
    anger_description = TextAreaField('분노 감정 설명', validators=[InputRequired()])
    disgust_description = TextAreaField('혐오 감정 설명', validators=[InputRequired()])
    neutral_description = TextAreaField('중립 감정 설명', validators=[InputRequired()])
    surprise_description = TextAreaField('놀람 감정 설명', validators=[InputRequired()])
    fear_description = TextAreaField('두려움 감정 설명', validators=[InputRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'genemo'
@app.route('/', methods=['GET', 'POST'])

def genemo():
    form1 = ConceptForm()
    form2 = PersonalizeStatus()
    form3 = EmotionCount()
    form4 = EmotionDescribe()
    
    if form1.validate_on_submit():
        session['concept'] = form1.concept.data
        return redirect(url_for('genemo'))

    if form2.validate_on_submit():
        session['status'] = form2.status.data
        if form2.status.data == 'yes':
            return redirect(url_for('genemo', step='step3'))
        else:
            return redirect(url_for('genemo', step='step5'))

    

    if form3.validate_on_submit():
        session['happiness'] = form3.happiness.data
        session['sadness'] = form3.sadness.data
        session['anger'] = form3.anger.data
        session['disgust'] = form3.disgust.data
        session['neutral'] = form3.neutral.data
        session['surprise'] = form3.surprise.data
        session['fear'] = form3.fear.data
        return redirect(url_for('genemo',step="step4"))
    
    if form4.validate_on_submit():  # 새로운 폼이 제출되면 해당 데이터를 세션에 저장
        session['happiness_description'] = form4.happiness_description.data
        session['sadness_description'] = form4.sadness_description.data
        session['anger_description'] = form4.anger_description.data
        session['disgust_description'] = form4.disgust_description.data
        session['neutral_description'] = form4.neutral_description.data
        session['surprise_description'] = form4.surprise_description.data
        session['fear_description'] = form4.fear_description.data

        data = f"Concept: {session.get('concept')}\n" \
               f"Status: {session.get('status')}\n" \
               f"Happiness: {session.get('happiness')}\n" \
               f"Sadness: {session.get('sadness')}\n" \
               f"Anger: {session.get('anger')}\n" \
               f"Disgust: {session.get('disgust')}\n" \
               f"Neutral: {session.get('neutral')}\n" \
               f"Surprise: {session.get('surprise')}\n" \
               f"Fear: {session.get('fear')}\n" \
               f"Happiness Description: {session.get('happiness_description')}\n" \
               f"Sadness Description: {session.get('sadness_description')}\n" \
               f"Anger Description: {session.get('anger_description')}\n" \
               f"Disgust Description: {session.get('disgust_description')}\n" \
               f"Neutral Description: {session.get('neutral_description')}\n" \
               f"Surprise Description: {session.get('surprise_description')}\n" \
               f"Fear Description: {session.get('fear_description')}"
        save_data_to_file(data)
        return redirect(url_for('genemo',step="step5"))


    return render_template('wizard.html', form1=form1, form2=form2, form3=form3,form4=form4,
                           concept=session.get('concept'),
                           status=session.get('status'),
                           happiness=session.get('happiness'),
                           sadness=session.get('sadness'),
                           anger=session.get('anger'),
                           disgust=session.get('disgust'),
                           neutral=session.get('neutral'),
                           surprise=session.get('surprise'),
                           fear=session.get('fear'),
                           describe=session.get('describe'))

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, render_template, redirect, url_for, session
# from flask_wtf import FlaskForm
# from wtforms import StringField, SelectField, IntegerField, TextAreaField
# from wtforms.validators import InputRequired, NumberRange
# from form import ConceptForm,PersonalizeStatus,EmotionCount,EmotionDescribe

# class ConceptForm(FlaskForm):
#     concept = StringField('Concept', validators=[InputRequired()])

# class PersonalizeStatus(FlaskForm):
#     status = SelectField('Personalize Status', choices=[('yes', 'Yes'), ('no', 'No')])

# class EmotionCount(FlaskForm):
#     happiness = IntegerField('Happiness', validators=[NumberRange(min=0,max=32)])
#     sadness = IntegerField('Sadness', validators=[NumberRange(min=0,max=32)])
#     anger = IntegerField('Anger', validators=[NumberRange(min=0,max=32)])
#     disgust = IntegerField('Disgust', validators=[NumberRange(min=0,max=32)])
#     neutral = IntegerField('Neutral', validators=[NumberRange(min=0,max=32)])
#     surprise = IntegerField('Surprise', validators=[NumberRange(min=0,max=32)])
#     fear = IntegerField('Fear', validators=[NumberRange(min=0,max=32)])
    
# class EmotionDescribe(FlaskForm):
#     describe = TextAreaField('Describe Emotion', validators=[InputRequired()])

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'genemo'



# @app.route('/', methods=['GET', 'POST'])
# def genemo():
#     form1 = ConceptForm()
#     form2 = PersonalizeStatus()
#     form3 = EmotionCount()
#     form4 = EmotionDescribe()
    

#     if form1.validate_on_submit():
#         session['concept'] = form1.concept.data
#         return redirect(url_for('genemo'))

#     if form2.validate_on_submit():
#         session['status'] = form2.status.data
#         if form2.status.data == 'yes':
#             return redirect(url_for('genemo', step='step3'))
#         else:
#             return redirect(url_for('genemo', step='step5'))

#     if form3.validate_on_submit():
#         session['happiness'] = form3.happiness.data
#         session['sadness'] = form3.sadness.data
#         session['anger'] = form3.anger.data
#         session['disgust'] = form3.disgust.data
#         session['neutral'] = form3.neutral.data
#         session['surprise'] = form3.surprise.data
#         session['fear'] = form3.fear.data
        

#         return redirect(url_for('genemo'))

#     if form4.validate_on_submit():
#         session['describe'] = form4.describe.data
        
#         return redirect(url_for('genemo'))
    
    

#     return render_template('wizard.html', form1=form1, form2=form2, form3=form3, form4=form4,
#                            concept=session.get('concept'), 
#                            status=session.get('status'),
#                            happiness=session.get('happiness'),
#                            sadness=session.get('sadness'),
#                            anger=session.get('anger'),
#                            disgust=session.get('disgust'),
#                            neutral=session.get('neutral'), 
#                            surprise=session.get('surprise'),
#                            fear=session.get('fear'), 
#                            describe=session.get('describe'))
    
    

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route("/")
# def step1():
#     return render_template("homepage.html")



# @app.route("/applyconcept")
# def step2():
#     inputconcept=ConceptForm(request.form)
#     print(inputconcept)
#     return render_template("personalize.html")

# @app.route("/exregister")
# def exregister():
#     inputconcept=request.args.get('inputconcept')
#     return redirect(url_for("register",inputconcept=inputconcept))

# # @app.route('/concept')
# # def concept():
# #     return render_template("결과창.html")


# @app.route('/applyemotion', methods=['GET', 'POST'])
# def register():
#     emotioncount = EmotionCount(request.form)
#     inputconcept=request.args.get('inputconcept')
#     if request.method == 'GET':
#         return render_template('count.html')
#     elif request.method == 'POST' and emotioncount.validates():
#         cnt = {
#             "Happiness": EmotionCount.happiness.data,
#             "Sadness": EmotionCount.sadness.data,
#             "Fear": EmotionCount.fear.data,
#             "Anger": EmotionCount.anger.data,
#             "Neutral": EmotionCount.neutral.data,
#             "Surprise": EmotionCount.surprise.data,
#             "Disgust": EmotionCount.disgust.data
#         }
#         return redirect(url_for('form_wizard', cnt=cnt, inputconcept=inputconcept))
        
    
    


# @app.route("/specific",methods=['GET','POST'])
# def form_wizard():

#     inputconcept=request.args.get('inputconcept')

#     cnt=request.args.get('cnt') 
#     cnt=ast.literal_eval(cnt) if cnt else {}
#     happiness_des={}
#     sadness_des={}
#     fear_des={}
#     anger_des={}
#     neutral_des={}
#     surprise_des={}
#     disgust_des={}
#     emotiondescribe=EmotionDescribe(request.form)
#     for i in range(cnt["Happiness"]):
#         happiness_text = EmotionDescribe()
#         if happiness_text.validate_on_submit():
#             happiness_des[f'{i+1}'] = happiness_text.describe.data
#     for i in range(cnt["Sadness"]):
#         sadness_text = EmotionDescribe()
#         if sadness_text.validate_on_submit():
#             sadness_des[f'{i+1}'] = sadness_text.describe.data
#     for i in range(cnt["Fear"]):
#         fear_text = EmotionDescribe()
#         if fear_text.validate_on_submit():
#             fear_des[f'{i+1}'] = fear_text.describe.data
#     for i in range(cnt["Anger"]):
#         anger_text = EmotionDescribe()
#         if anger_text.validate_on_submit():
#             anger_des[f'{i+1}'] = anger_text.describe.data
#     for i in range(cnt["Nutral"]):
#         neutral_text = EmotionDescribe()
#         if neutral_text.validate_on_submit():
#             neutral_des[f'{i+1}'] = neutral_text.describe.data
#     for i in range(cnt["Surprise"]):
#         surprise_text = EmotionDescribe()
#         if surprise_text.validate_on_submit():
#             surprise_des[f'{i+1}'] = surprise_text.describe.data
#     for i in range(cnt["Disgust"]):
#         disgust_text = EmotionDescribe()
#         if disgust_text.validate_on_submit():
#             disgust_des[f'{i+1}'] = disgust_text.describe.data
#     return redirect(url_for("result",cnt=cnt,inputconcept=inputconcept))

# @app.route("/result")
# def step3():
#     return render_template("result.html")

# @app.route("/Genemo")
# def Genemo():
#     return redirect(url_for('step1'))


# @app.route("/start")
# def start():
#     return render_template("start.html")

# @app.route("/contribution")
# def contribution():
#     return render_template("contribution.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route('/', methods=['GET','POST'])
# def startconcept():# 핵심 컨셉 작성 
#     concept = ConceptForm()

#     if concept.validate_on_submit():

#         text = concept.concept.data

#         return redirect(url_for('step2'),text=text)
    
#     return render_template('index.html')

# @app.route('/step2', methods=['GET','POST'])
# def step2(): #추가 개인화 여부 
#     status = PersonalizeStatus()
#     text = text

#     if status.validate_on_submit():

#         if status.status.data == 'yes':
#             return redirect(url_for('step3'))
#         else:
#             return redirect(url_for('step5'))
    
#     return render_template('index.html', text=text)

# @app.route('/step3', methods=['GET','POST'])
# def step3(): # 감정별 갯수 세기 
#     ecnt = EmotionCount()
#     text = text 
#     cnt = {}


#     if ecnt.validate_on_submit():

#         cnt['Happiness'] = ecnt.happiness.data
#         cnt['Sadness'] = ecnt.sadness.data
#         cnt['Anger'] = ecnt.anger.data
#         cnt['Disgust'] = ecnt.disgust.data
#         cnt['Neutral'] = ecnt.neutral.data
#         cnt['Surprise'] = ecnt.surprise.data
#         cnt['Fear'] = ecnt.fear.data

#         return redirect(url_for('step4', cnt =cnt ))

#     return render_template('index.html', text=text, cnt=cnt )


# @app.route('/step4', methods=['GET','POST'])
# def step4(): # 세부 감정 기입  
#     desc = EmotionDescribe()
#     text = text 
#     cnt = cnt


#     if desc.validate_on_submit():

        

#         return redirect(url_for('step4', desc=desc ))

#     return render_template('index.html', text=text, cnt=cnt )

# @app.route('/step5', methods=['GET','POST'])
# def step5(): # 생성하기   
    
#     if desc.validate_on_submit():

        

#         return redirect(url_for('step4', cnt =cnt ))

#     return render_template('index.html', text=text, cnt=cnt )

# if __name__=="__main__":
#     app.run(debug=True)