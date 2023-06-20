# Welcome to Ge-Nemo Frontend

Ge-Nemo의 프론트엔드는 ReactJS를 기반으로(create-react-app) 개발되었습니다.\
genemo-front 디렉터리는 배포를 위해 build한 결과를 반영합니다.

react app을 위한 모든 종속 패키지들은 `package.json`에 포함되어 있으며,\
node_modules는 gitignore에 포함되어 있어 숨겨져 있습니다.

### 구성 디렉터리/파일들 소개
- config : flask와 연동을 위해 `npm run eject` 실행 후 기본 환경 설정을 수정한 파일들이 들어있는 폴더
- public/index.html : 기본 html 파일
- src/App.js : Header와 FormWizard 컴포넌트 정의
- src/index.js : html 파일의 'root'에 App.js에 들어있는 컴포넌트들(Header와 FormWizard)를 렌더링 함
- index.css : 웸페이지 전체에 적용되는 스타일 속성 정의(폰트 등)
- App.css : App.js에 포함되어 있는 모든 컴포넌트들의 스타일 속성 정의
