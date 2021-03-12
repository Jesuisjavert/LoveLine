# SSAFY Bigdata project

## How to Run

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyse.py
python visualize.py
```

### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
# requirements.txt가 안되는 경우엔 개별적으로 설치를 해줘야한다 보통 pandas,scipy,scikit-learn 패키지가 문제를 일으키는경우가 많다.
# 패키지 설치시 동반설치되는 패키지가 지원되지않는 확장자를 가져오는경우가 있어서 그럴때에는 개별설치를 추천한다.
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve

```
