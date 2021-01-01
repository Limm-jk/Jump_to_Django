# 장고 속성 바텀업
[점프 투 장고](https://wikidocs.net/book/4223) 사이트를 보며 실습하는 저장소입니다.

## 실행
```
# 가상환경
. ./mysite/Scripts/activate
# 의존성
pip freeze -r > requirements.txt
# 서버 실행
./runserver
```

## Docker
```
# 도커 연동 DB 설정
docker-compose exec web python manage.py migrate
```

## 모델 설정