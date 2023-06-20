import openai
import os
import json 

#현재 파일의 상위 디렉토리 경로 BASE_DIR 변수에 저장
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#API 키 비밀 정보 포함
secret_file = os.path.join(BASE_DIR+'\\genemo-back', 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


openai.api_key = secrets['open_ai']

#주어진 한국어 텍스트 영어로 번역하여 명사구 형태로 추출
def translate_concept(input_text):
    prompt = "번역: stable diffusion에서 prompt로 이용할 수 있도록 명사구의 형태로 한국어에서 영어로 번역해주세요. \n한국어: " + input_text + "\n영어: "
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    translated_text = response.choices[0].text.strip()
    return translated_text



#주어진 한국어 텍스트 영어로 번역하여 수식어구 형태로 추출
def translate_describe(input_text):
    prompt = "번역: 대부분 행동 묘사와 관련된 표현이 입력 될 건데 stable diffusion에서 prompt로 이용할 수 있도록, 또 수식어구의 형태로, 한국어에서 영어로 번역해주세요.\n한국어: " + input_text + "\n영어: "
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    translated_text = response.choices[0].text.strip()
    return translated_text

