from flask import Flask

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/concept')
def concept():
    return '컨셉을 입력하세요 '

@app.route('/personalize')
def personalize():
    return '추가 개인화 여부'

@app.route('/emotion')
def emotion():
    return '감정 구성하기'

@app.route('/emotion/specific')
def specific():
    return '감정 별 묘사하기'

@app.route('/result')
def result():
    return '결과 확인'