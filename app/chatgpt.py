import openai

openai.api_key = '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'

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

# input_text = input("번역할 한국어 텍스트를 입력하세요: ")
# # translated_text = translate_concept(input_text)
# # print("번역 결과: ", translated_text)


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

input_text = input("번역할 한국어 텍스트를 입력하세요: ")
translated_text = translate_describe(input_text)
print("번역 결과: ", translated_text)
