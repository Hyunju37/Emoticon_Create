from flask import Flask, render_template, redirect, url_for, session, request,make_response
#from flask_wtf import FlaskForm
#from wtforms import StringField, SelectField, IntegerField, TextAreaField
#from wtforms.validators import InputRequired, NumberRange, ValidationError
#from chatgpt import openai
#from form import ConceptForm, PersonalizeStatus,EmotionCount,EmotionDescribe
import os
import urllib.parse
# 파일 저장 함수
def save_data_to_file(data):
    filename = 'data.txt'
    with open(filename, 'w',encoding='utf-8') as file:
        file.write(data + '\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'genemo'

@app.route('/', methods=['GET'])
def genemo_index():
   return render_template("index.html")


@app.route('/', methods=['POST'])
def genemo():
    #form1 = ConceptForm()
    #form2 = PersonalizeStatus()
    #form3 = EmotionCount()
    #form4 = EmotionDescribe()
    
    
    info = request.get_json()
    print(info)

    if info['mode'] == 0:
        data = f"Concept: {info['formData']}\n" \
                f"Status: {info['mode']}\n"
    else:
        data = f"Concept: {info['formData']}\n" \
                f"Status: {info['mode']}\n" \
                f"Happiness: {info['numbers'][0]}\n" \
                f"Sadness: {info['numbers'][1]}\n" \
                f"Anger: {info['numbers'][2]}\n" \
                f"Fear: {info['numbers'][3]}\n" \
                f"Surprise: {info['numbers'][4]}\n" \
                f"Disgust: {info['numbers'][5]}\n" \
                f"Neutral: {info['numbers'][6]}\n" \
                f"Happiness Description: {info['descs'][0]}\n" \
                f"Sadness Description: {info['descs'][1]}\n" \
                f"Anger Description: {info['descs'][2]}\n" \
                f"Fear Description: {info['descs'][3]}\n" \
                f"Surprise Description: {info['descs'][4]}\n" \
                f"Disgust Description: {info['descs'][5]}\n" \
                f"Neutral Description: {info['descs'][6]}\n"
    
    save_data_to_file(data)
    response=make_response()
    response.set_cookie('input_data', urllib.parse.quote(data))
    
    return response





if __name__ == '__main__':
    app.run(debug=True)


    


