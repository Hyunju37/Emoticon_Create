# Welcome to GeNemo-Backend

<h3>GeNemo의 백엔드는 Flask를 기반으로 개발되었습니다.</h3>
genemo-backend는 모델을 백엔드 시스템과 연동,입력 데이터 처리, 모델 실행,결과 반환 등 실제 운영 환경에서 사용 할수 있게 하였습니다.<br>
<br>
주요 모델인 chatgpt,stablediffusion의 가중치 구조 파라미터를 저장합니다.<br>
<br>
app.py 실행을 위한 패키지는 requirements.txt 파일에 저장되어 있습니다.<br>


<h2>구성 디렉토리 파일들 소개</h2>
● 'app.py' :주요 실행 파일로, genemo-backend 실행 로직이 구현되어 있습니다.<br>
● 'static\react' : 정적 파일(CSS,JavaScript,이미지 등)이 위치하는 디렉토리입니다.<br>
● 'templates' : HTML 템플릿 파일이 위치하는 디렉토리입니다.<br>
● 'chatgpt' : 입력된 텍스트를 프롬트프에 적용하기위해 구조에 맞게 가공하여 번역해주는 파일입니다.<br>
● 'stable.py': stable diffusion 모델에 맞춰 이미지 저장, 시각화 기능을 작성한 파일입니다.



