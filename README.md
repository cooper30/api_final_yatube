# Описание

Это проект API для соц. сети дневников Yatube. 
В проекте реализована работа с постами , комментариями, группами и подписками. 
Документация API доступна по адресу http://127.0.0.1:8000/redoc/


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/cooper30/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Примеры запросов

POST api/v1/jwt/create/
Ответ:
```
{
  "refresh": "string",
  "access": "string"
}
```

GET api/v1/groups/
Ответ:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

GET /api/v1/posts/
Ответ:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

GET api/v1/posts/{post_id}/comments/{id}/
Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

GET api/v1/follow/
Ответ:
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

Документация API доступна по адресу /redoc/