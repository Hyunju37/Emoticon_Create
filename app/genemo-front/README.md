# Welcome to Ge-Nemo Frontend

Ge-Nemo의 프론트엔드는 ReactJS를 기반으로(create-react-app) 개발되었습니다.\
genemo-front 디렉터리 및 genemo-back 디렉터리는 배포를 위해 리액트 어플을 build한 결과를 반영합니다.

react app을 위한 모든 종속 패키지들은 `package.json`에 포함되어 있으며,\
node_modules는 gitignore에 포함되어 있어 숨겨져 있습니다.

### 구성 디렉터리/파일들 소개
- config : flask와 연동을 위해 `npm run eject` 실행 후 기본 환경 설정을 수정한 파일들이 들어있는 폴더
- public/index.html : 기본 html 파일
- src/App.js : Header와 FormWizard 컴포넌트 정의
- src/index.js : html 파일의 'root'에 App.js에 들어있는 컴포넌트들(Header와 FormWizard)를 렌더링 함
- index.css : 웸페이지 전체에 적용되는 스타일 속성 정의(폰트 등)
- App.css : App.js에 포함되어 있는 모든 컴포넌트들의 스타일 속성 정의

### 특징
Ge-Nemo의 웹페이지는 사용자의 이용 편의성을 높이기 위해 Form-Wizard 스타일을 반영했습니다.\
Form-Wizard는 이모티콘 생성의 전 과정을 위한 컴포넌트이고 step값이 현재 단계 값을 저장합니다.\
진행 단계 시각화는 `react-step-progress-bar`(https://www.npmjs.com/package/react-step-progress-bar) 패키지를 추가해 사용했습니다.

### Flask와의 상호 작용
axios를 이용해 flask측으로 요청을 보내고 응답을 받습니다. 사용자가 어떤 모드를 선택하느냐에 따라 보내는 데이터의 종류와 시점이 달라집니다.\
간편 모드의 경우 사용자가 입력한 컨셉 문장이 2단계에서 '생성하기' 버튼을 누르는 순간 POST 방식으로 데이터를 전송하며\
개인화 모드의 경우 컨셉, 감정별 장수, 감정별 묘사들이 4단계에서 '생성하기' 버튼을 누르는 순간 전송됩니다.\
참고 함수:
```
sendDataToServer0
sendDataToServer1
```
이미지 생성 과정이 생성 중인지, 완료되었는지 flask측에 일정 주기로 물어보면서 완료되었다는 응답이 넘어온 순간 Form Wizard 상의 step이 1 증가하면서, 로딩 창에서 결과 창으로 넘어갑니다.
참고 함수:
```
getDataFromServer
```
만들어진 이모티콘을 웹 상에서 보고, 다운로드 받는 기능 역시 서버측에 특정 라우트로 요청을 보내 이미지 데이터를 전달 받습니다.
참고 함수:
```
getImageUrl
downloadImages
```
