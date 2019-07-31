# Privacy Management Program
# *for python 3*
------



## 1.주제 소개
**PMP(Privacy Management Program)** 는, 사용자의 정보 유출을 방지하는 프로그램이다.

사용자 컴퓨터 내에 다양한 포맷으로 존재하는 각종 정보들을 사용자 키워드를 통해 검색하고, 필터링하여 악성 사용자가 해당 정보를 탈취하지 못하게 방지하는 것이 목표이다.

----

## 2.주요 기능
1.**Whole File Scan** : 지정경로 내 개인정보 포함 문서, 이미지 파일 스캔

###### 대상항목: txt, docx, xlsx, pptx, png, bmp, jpg, gif

2.**Real-Time Monitoring**: 개인정보 포함 문서 파일의 열람, 복사 실시간 감시 및 방지.
복사된 텍스트 데이터 실시간 감시 및 붙여넣기 방지

###### 대상항목: txt, docx, xlsx, pptx

----

## 3.프로그램 동작 화면

###### Windows OS 환경에 맞춰서 개발완료되었으며 Python 3.7 버전사용
###### 테스트환경 - Windows 7 32bit , Windows 10 64bit




#### 3.1 First Setting
- 처음 프로그램을 시작시 레지스트리 세팅을하고 패스워드 세팅을 하는 모습입니다.


<레지스트리 편집>


![레지스트리편집](https://github.com/kseymin/python_pmp/blob/master/README_Resources/firstStart_Autoset.png "레지스트리편집")


<패스워드 설정>

![패스워드설정](https://github.com/kseymin/python_pmp/blob/master/README_Resources/fistStart_PasswordSetting.png "패스워드설정")


- 개인정보로 분류할 규칙을 지정합니다.
  ######  *규칙 은 정규표현식 및 일반텍스트로 분류합니다.*




<규칙설정>

![규칙설정](https://github.com/kseymin/python_pmp/blob/master/README_Resources/ruleSet01.png "규칙설정")


<규칙설정추가>

![규칙설정추가](https://github.com/kseymin/python_pmp/blob/master/README_Resources/ruleSet03_add.png "규칙설정추가")




#### 3.2 Main
- 메인 화면 입니다. 위에는 탭으로 홈화면,룰세팅,도움말 을 볼수있으며
아래에는 시스템상에서 분류하는기능, 실시간 프로세스 관리등을 맡고있는 기능 버튼이있습니다.
프로그램 각기능의 처리 는 가운데 로고 화면에 나오게 됩니다.


<메인화면>

![메인화면](https://github.com/kseymin/python_pmp/blob/master/README_Resources/main.png "메인화면")



#### 3.3 Whole Searching
- 시스템상에서 개인정보가 들어있는 문서, 이미지를 추출해줍니다.



<경로설정>


![경로설정](https://github.com/kseymin/python_pmp/blob/master/README_Resources/wholeSearch01.png "경로설정")



<실행중화면>


![실행중화면](https://github.com/kseymin/python_pmp/blob/master/README_Resources/wholeSearch03_Running.png "실행중화면")



<결과화면>


![결과화면](https://github.com/kseymin/python_pmp/blob/master/README_Resources/wholeSearch02_Result.png "결과화면")


#### 3.4 Real time Searching
- 현재 프로세스를 계속해서 탐지 및 검출하여 문서 프로그램일 시 개인정보로 분류된 텍스트가
쓰이지 않게 제한을합니다,
또한 개인정보 로 분류된 텍스트, 파일을 복사, 붙여넣기 기능을 쓰지 못하도록 막습니다.



<실시간탐지>


![실시간탐지](https://github.com/kseymin/python_pmp/blob/master/README_Resources/realTime01.png "실시간탐지")



<개인정보를 다룰시 프로세스를 종료한 모습>


![개인정보검출](https://github.com/kseymin/python_pmp/blob/master/README_Resources/realTime01.png "개인정보검출")



-패스워드 입력시 해당 문서 는 계속 작업을 할 수 있게 예외로 처리합니다.




 <개인정보가 들어간 문서를 복사방지>


 ![실시간문서복사방지1](https://github.com/kseymin/python_pmp/blob/master/README_Resources/realTime03_copyDetect.png "문서복사방지1")



 ![실시간문서복사방지2](https://github.com/kseymin/python_pmp/blob/master/README_Resources/realTime04_copyDisable.png "문서복사방지2")

 ------

 ### 개발 기간
 >약 1개월

 총 4명의 팀원 으로 이루어 져서 개발
 -> 제가 맡은 부분은 실시간 탐지 기능 부분 ,프로그램 최적화 부분


-----

 ### 참고 문헌

> - 사이트
 https://support.office.com/ : MS Office Product Support
 https://docs.microsoft.com/ : Microsoft Windows Developer Center
 http://pyqt.sourceforge.net/Docs/PyQt5/ : PyQt5 Reference Guide
 https://github.com/tesseract-ocr/tesseract: Tesseract-OCR GitHub


>- 서적
 점프 투 파이썬 - 박응용 저, 이지스 퍼블리싱
 리버싱 핵심원리 – 이승원 저, 인사이트
