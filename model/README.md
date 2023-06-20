# model 

- 모델에서는 3개의 파일로 텍스트 프롬프트에 입력하여, 이미지를 생성하고, 이모티콘에 맞게 이미지를 설정한다.
- fine_tuning : 감정 데이터 셋 훈련, 텍스트 프롬프트를 입력받아 이미지 생성, 조건에 맞는 이미지 설정한다. create.png 파일 생성.
- sementic_segmentation : 객체와 배경 이미지를 분리한다. create.png 파일을 받아 mask 이미지인 mask.png 생성. create.png 파일을 sementic_segmentation 한다.
- background_transparent : create.png와 mask.png을 이용하여 mask가 완료된 이미지 생성. 이후, 그 이미지의 배경을 투명화하여, output.png 생성.
- output.png가 이모티콘 이미지의 최종 생성 결과물이다.
--------
- 참고 : fine_tuning까지 과정은 해결, sementic_segmentation, background_transparent은 개발 중.
