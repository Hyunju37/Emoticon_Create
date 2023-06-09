from flask import Flask, render_template,request,redirect,url_for
import sys
from form import ConceptForm,EmotionCount,EmotionDescribe
import ast
# con=ConceptForm()
# con1=EmotionCount()
# con2=EmotionDescribe()


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