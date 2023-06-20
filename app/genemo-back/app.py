from flask import Flask, render_template, redirect, url_for, session, request,make_response,send_file, g
from chatgpt import translate_concept,translate_describe
from stable import save_images, plot_images
from PIL import Image
from expressions import V
import os
import urllib.parse
import openai
import keras_cv
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import zipfile



# 파일 저장 함수
def save_data_to_file(data):
    filename = 'data.txt'
    with open(filename, 'w',encoding='utf-8') as file:
        file.write(data + '\n')
#Flask application 실행
app = Flask(__name__)
app.config['SECRET_KEY'] = 'genemo'

waiting = 'notyet'

#URL에 대한 GET 요청 처리,index.html    
@app.route('/', methods=['GET'])
def genemo_index():
   return render_template("index.html")

#URL에 대한 POST 요청 처리
@app.route('/', methods=['POST'])
def genemo():

#stable diffusion 모델 삽입 
    keras.mixed_precision.set_global_policy("mixed_float16") #혼합 정밀도 
    model = keras_cv.models.StableDiffusion(jit_compile=True) #stablediffusion 모델 생성 model에 할당
#신경망 모델에 데이터셋 미리 학습된 가중치 로드 
    model.diffusion_model.load_weights('finetuned_stable_diffusion2e.h5')
    info = request.get_json()
    data=""
    
#컨셉 입력 번역
    T=translate_concept(f"{info['formData']}\n")
#이모티콘 간편모드 실행
    if info['mode'] == 0:
        data += f"{info['formData']}\n" #데이터 변수에 폼 데이터 추가
        
        generated_images = [] #생성된 이미지 저장할 리스트 생성
        for i in range(32):
            generated_images.append(model.text_to_image(T+" "+V[i],batch_size=1))
        save_images(generated_images)   

#이모티콘 추상화모드 실행     
    else:

        data+="\n"
        data+= "\n".join(f"{info['formData']},{info['numbers'][i]},{info['descs'][i]}" for i in range(7)) 
        
        a=info['descs'][0]   #행복 감정 입력 폼
        b=info['descs'][1]   #슬픔 감정 입력 폼
        c=info['descs'][2]   #분노 감정 입력 폼
        d=info['descs'][3]   #두려움 감정 입력 폼
        e=info['descs'][4]   #놀람 감정 입력 폼
        f=info['descs'][5]   #역겨움 감정 입력 폼
        g=info['descs'][6]   #중립 감정 입력 폼

#생성하고 싶은 감정의 종류의 개수에 따른 입력문 추가
        a1=[]
        for i in range(info['numbers'][0]):
            a1.append(a[i])
        print(a1)

        b1=[]
        for i in range(info['numbers'][1]):
            b1.append(b[i])
        print(b1)

        c1=[]
        for i in range(info['numbers'][2]):
            c1.append(c[i])
        print(c1)

        d1=[]
        for i in range(info['numbers'][3]):
            d1.append(d[i])
        print(d1)

        e1=[]
        for i in range(info['numbers'][4]):
            e1.append(e[i])
        print(e1)

        f1=[]
        for i in range(info['numbers'][5]):
            f1.append(f[i])
        print(f1)
        g1=[]
        for i in range(info['numbers'][6]):
            g1.append(g[i])
        print(g1)
        
        # 입력된 총 32개의 각각 입력된 감정의 종류들 번역
        translated_text = []  
        for i in range(info['numbers'][0]):
            translation =translate_describe(a1[i])
            translated_text.append(translation+ " "+"Happiness")
        for i in range(info['numbers'][1]):
            translation = translate_describe(b1[i])
            translated_text.append(translation+" "+"Sadness")
        for i in range(info['numbers'][2]):
            translation = translate_describe(c1[i])
            translated_text.append(translation+" "+"Anger")
        for i in range(info['numbers'][3]):
            translation = translate_describe(d1[i])
            translated_text.append(translation+" "+"Fear")
        for i in range(info['numbers'][4]):
            translation = translate_describe(e1[i])
            translated_text.append(translation+" "+"Surprise")
        for i in range(info['numbers'][5]):
            translation = translate_describe(f1[i])
            translated_text.append(translation+" "+"Disgust")
        for i in range(info['numbers'][6]):
            translation = translate_describe(g1[i])
            translated_text.append(translation+" "+"Neutral")
        print("번역 결과: ", translated_text)
        
        #가공된 입력문 stable diffusion 모델에 삽입
        generated_images = []
        for translation in translated_text:
            generated_images.extend(model.text_to_image(T + " " + translation, batch_size=1))
        
        save_images(generated_images) #생성된 이미지 generated_images경로로 저장
    save_data_to_file(data) #컨셉 or 개인화에서 입력된 Text data.txt 형태로 저장 
    response=make_response()
    response.set_cookie('input_data', urllib.parse.quote(data)) #컨셉 or 개인화에서 입력된 Text 웹 브라우저 쿠키값 생성


    global waiting
    waiting='done'

    return response
#컨셉 or 개인화 입력 후 모델에 입력된 생성 진행중 waiting' or 진행이 완료되면 결과 확인으로 이동
@app.route('/yet', methods=['GET'])
def done_yet():
    
    global waiting
    return waiting
#이미지 저장 경로 설정
@app.route('/img/<int:image_index>')
def serve_image(image_index):
    image_path = f'generated_images/image_{image_index}.jpg'
    return send_file(image_path, mimetype='image/jpeg')

#웹에서 이미지 저장 파일 버튼 ==>자신이 원하는 경로에  images.zip 파일로 저장
@app.route('/img/download')
def download_images():
    images_directory = 'generated_images'
    zip_filename = 'images.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for image_filename in os.listdir(images_directory):
            image_path = os.path.join(images_directory, image_filename)
            zipf.write(image_path, image_filename)
    return send_file(zip_filename, mimetype='application/zip', as_attachment=True)
    



if __name__ == '__main__':
    app.run(debug=True)