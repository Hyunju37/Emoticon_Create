# Welcome to Ge-Nemo App!

사용자를 위한 맞춤형 이모티콘 32장을 생성해 주는 Ge-Nemo 서비스는 웹을 기반으로 동작하며
프론트엔드에 ReactJS, 백엔드에 Flask 프레임워크로 구성되어 있습니다.
이곳 App 디렉터리는 웹 어플리케이션 구성을 위해 만들어진 디렉터리로
사용자가 마주하는 웹 화면, 사용자로부터 입력 데이터를 받아 text2image 모델로 만들어진 결과 이모티콘들을 사용자 측으로 내보내는 모든 과정이 담겨 있습니다.

## 디렉터리/파일 설명
- genemo-back: flask 기반으로 구성된 back-end
- genemo-front: react을 기반으로 구성된 front-end
- nginx.conf: nginx 웹 서버 구성을 위한 파일
- requirements.txt: 필요 패키지들의 버전 관리를 위한 파일

## 사용 방법
### `pip install requirements.txt` 
필요 패키지들 한번에 설치
### `python app.py` 
react app을 제공

## 참여 팀원
- Back-end: 최윤수 https://github.com/Choiyounsou
- Front-end: 성현주 https://github.com/Hyunju37
- Server 및 배포: 김지우 https://github.com/kingjiwoo

## 참고자료
Flask-React 연동
https://www.youtube.com/watch?v=YW8VG_U-m48&t=223s
