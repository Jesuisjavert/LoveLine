# backend



가상환경 셋팅

```text
python -m venv venv
```

가상환경 접속

```text
source venv/Scripts/activate/
```



데이터 저장

```
datapreprocessing 폴더에서
## parse.py에서 pandas 패키지를 쓰기 때문에, pandas를 설치해줘야한다.
pip install pandas
python parse.py 실행
```

```text
/// backend 폴더에서 가상환경에서 접속하고 해야할것들

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata community.json
python manage.py initialize
```



더미데이터 넣는법

```
python manage.py dummydatainput
```

