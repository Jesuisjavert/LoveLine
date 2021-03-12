# Scrapy

> Scrapy는 Scraping을 도와주기위한 파이썬 기반 라이브러리이다.
>
> Scrapy를 이용하여 필요한 페이지로 접속하여 원하는 형태로 데이터를 가공하여 데이터를 저장할수 있도록 도와준다.



### Scrapy 설치

```
pip install scrapy
```



### Scrapy 프로젝트 생성

```
scrapy startproject { project 이름 }
```



### Scrapy 구조

- Spider
  - 어떤 웹 사이트를 어떻게 크롤링할 것인지 명시
  - 데이터 수집을 위한 수행 코드를 정의
  
- Selector
  - 웹 페이지에 HTML 요소를 간편하게 선택할 수 있도록 하는 클래스
  - CSS 선택자, XPath를 사용할 수 있음

- Item
  
  - 웹 페이지에 원하는 부분을 스크랩하여 저장할 때 사용하는 사용자 정의 자료구조 클래스
  
- Item Pipeline
  
  - 수집된 데이터 처리 방식 정의(파일저장/DB저장/이메일발송 등)
  
- Settings
  - Spider나 Item Pipeline 등이 어떻게 동작하도록 할 지에 대한 세부적인 설정사항
  - 프로젝트 모듈간 연결 및 기본 설정 정의
  
- middleware
  - 미들웨어란 보통 흐름, 처리 과정중 중간에 삽입되어 무언가를 처리하는 것





# Selenium

> Selenium은 주로 웹앱을 테스트하는데 이용하는 프레임워크다. `webdriver`라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.
>
> 브라우저를 직접 동작시킨다는 것은 JavaScript를 이용해 비동기적으로 혹은 뒤늦게 불러와지는 컨텐츠들을 가져올 수 있다는 것이다



### Selenium 설치

```
pip install selenium
```

