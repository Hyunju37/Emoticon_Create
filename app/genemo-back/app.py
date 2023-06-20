from flask import Flask, render_template, redirect, url_for, session, request,make_response,send_file, g
from chatgpt import translate_concept,translate_describe

import os
import urllib.parse
import openai
import keras_cv
import keras
from stable import save_images, plot_images
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import zipfile
from expressions import V


# 파일 저장 함수
def save_data_to_file(data):
    filename = 'data.txt'
    with open(filename, 'w',encoding='utf-8') as file:
        file.write(data + '\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'genemo'

waiting = 'notyet'
    
@app.route('/', methods=['GET'])
def genemo_index():
   return render_template("index.html")

#@app.before_request
#def waiting_default():
#    g.waiting = 1

@app.route('/', methods=['POST'])
def genemo():
    keras.mixed_precision.set_global_policy("mixed_float16")
    model = keras_cv.models.StableDiffusion(jit_compile=True)

    info = request.get_json()
    data=""
    


    if info['mode'] == 0:
        data += f"{info['formData']}\n" 
        T=translate_concept(f"{info['formData']}\n")
        generated_images = []
        for i in range(1):
            generated_images.append(model.text_to_image(T+" "+V[i],batch_size=1))
        print(T)
        save_images(generated_images)        
    else:
        data+="\n"
        data+= "\n".join(f"{info['formData']},{info['numbers'][i]},{info['descs'][i]}" for i in range(7)) 
        T=translate_concept(f"{info['formData']}\n")
        a=info['descs'][0]
        b=info['descs'][1]
        c=info['descs'][2]
        d=info['descs'][3]
        e=info['descs'][4]
        f=info['descs'][5]
        g=info['descs'][6]
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
        generated_images = []
        
        generated_images.extend(model.text_to_image(T + " " + translated_text[0], batch_size=1))
        generated_images.extend(model.text_to_image(T + " " + translated_text[1], batch_size=1))
        generated_images.extend(model.text_to_image(T + " " + translated_text[2], batch_size=1))
        save_images(generated_images)
    save_data_to_file(data)
    response=make_response()
    response.set_cookie('input_data', urllib.parse.quote(data))
    global waiting
    waiting='done'
    return response

@app.route('/yet', methods=['GET'])
def done_yet():
    #return g.waiting
    global waiting
    return waiting

@app.route('/img/<int:image_index>')
def serve_image(image_index):
    image_path = f'generated_images/image_{image_index}.jpg'
    return send_file(image_path, mimetype='image/jpeg')

#for i in range(32):
#    app.add_url_rule(f'/img/{i}', view_func=serve_image, methods=['GET'])

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