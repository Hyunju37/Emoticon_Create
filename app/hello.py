from flask import Flask, request, render_template, redirect, url_for, abort
from flask.typing import ResponseReturnValue
from flask.views import View

app = Flask(__name__, template_folder='templates')

@app.route('/index')
@app.route('/')
def index():
    return 'index'

@app.route('/concept')
def concept():
    return '컨셉을 입력하세요 '

@app.route('/personalize')
def personalize():
    return '추가 개인화 여부'

@app.route('/emotion/<kind>')
def emotion(kind):
    return kind

@app.route('/emotion/specific')
def specific():
    return '감정 별 묘사하기'

@app.route('/result')
def result():
    return '결과 확인'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form() 

@app.route('/hello/')
@app.route('/hello/<name>/')    
def hello(name=None):
    return render_template('hello.html', name=None)


#리다이렉션과 에러
#url_for => 함수 이름을 넣으면 해당 라우팅 URL을 반환
#redirect 반환받은 주소로 다시 http요청 
#abort 403 에러 발생 
# @app.errorhandler => 403에러 처리 

@app.errorhandler(403)
def permission_denied(error):
    return '403', 403

@app.route('/a/')
def a():
    return redirect(url_for('user_list'))

@app.route('/users')
def user_list():
    abort(403)

#플러거블 뷰
# 장고의 class 기반 뷰에서 영향을 받아 만들어짐

@app.route('/members/')
def mem_list():
    mems = []
    return render_template('mems.html',mems= mems)

class MemList(View):
    def dispatch_request(self):
        mems = []
        return render_template('mems.html', mems=mems)
    
app.add_url_rule('/members', view_func=MemList.as_view('mems_list'))
