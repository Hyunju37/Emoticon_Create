from flask import Flask, render_template,request,redirect,url_for
import sys
from form import ConceptForm,EmotionCount,EmotionDescribe, PersonalizeStatus
import ast

app=Flask(__name__)
app.config["SECRET_KEY"]='genemo'


######
@app.route('/', methods=['GET','POST'])
def form_wizard():# 핵심 컨셉 작성 
    concept = ConceptForm()

    if concept.validate_on_submit():

        text = concept.concept.data

        return redirect(url_for('step2'))
    
    return render_template('index.html', text=text)

@app.route('/step2', methods=['GET','POST'])
def step2(): #추가 개인화 여부 
    status = PersonalizeStatus()

    text = text

    if status.validate_on_submit():

        if status.status.data == 'O':
            return redirect(url_for('step3'))
        else:
            return redirect(url_for('step5'))
    
    return render_template('index.html', text=text)

@app.route('/step3', methods=['GET','POST'])
def step3(): # 감정별 갯수 세기 
    ecnt = EmotionCount()
    text = text 
    cnt = {}


    if ecnt.validate_on_submit():

        cnt['Happiness'] = ecnt.happiness.data
        cnt['Sadness'] = ecnt.sadness.data
        cnt['Anger'] = ecnt.anger.data
        cnt['Disgust'] = ecnt.disgust.data
        cnt['Neutral'] = ecnt.neutral.data
        cnt['Surprise'] = ecnt.surprise.data
        cnt['Fear'] = ecnt.fear.data

        return redirect(url_for('step4', cnt =cnt ))

    return render_template('index.html', text=text, cnt=cnt )


@app.route('/step4', methods=['GET','POST'])
def step4(): # 세부 감정 기입  
    desc = EmotionDescribe()
    text = text 
    cnt = cnt
    set_describe = {}

    if desc.validate_on_submit():
        # EmotionDescribe 폼에 있는 필드를 반복하여 데이터 가져오기
        for field_name in desc.field_names:
            field = getattr(desc, field_name)
            set_describe[field_name] = field.data


        

        return redirect(url_for('step5', set_describe=set_describe ))

    return render_template('index.html', text=text, cnt=cnt, set_describe=set_describe )

@app.route('/step5', methods=['GET','POST'])
def step5(): # 생성하기   
    


    if desc.validate_on_submit():

        

        return redirect(url_for('step4', cnt =cnt ))

    return render_template('index.html', text=text, cnt=cnt )




#####




@app.route("/specific")
def specific():
    inputconcept=request.args.get('inputconcept')

    cnt=request.args.get('cnt') 
    cnt=ast.literal_eval(cnt) if cnt else {}
    happiness_des={}
    sadness_des={}
    fear_des={}
    anger_des={}
    neutral_des={}
    surprise_des={}
    disgust_des={}
    emotiondescribe=EmotionDescribe(request.form)
    for i in range(cnt["Happiness"]):
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
    return redirect(url_for("result",cnt=cnt,inputconcept=inputconcept))

@app.route("/result")
def step3():
    return render_template("result.html")




if __name__=="__main__":
    app.run(debug=True)