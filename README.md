# api_yatube

### Используется:

[![Python](https://img.shields.io/badge/-Python_3.7.9-464646??style=flat-square&logo=Python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django](https://img.shields.io/badge/-Django_rest_framework_3.12.4-464646??style=flat-square&logo=Django)](https://www.django-rest-framework.org)

## Описание

###### Данный проект является домашней работой в рамках обучения в Яндекс.Практикум, модуль знакомства с API. В функционал входит макет учебного проекта yatube, а так же полноценно работающий CRUD.


# Взаимодействие
<details><summary>Эндпоинты для взаимодействия</summary>

 
Передаём логин и пароль, получаем токен.
```
api/v1/api-token-auth/ (POST)
```
 

Получаем список всех постов или создаём новый пост.
```
api/v1/posts/ (GET, POST)
```
 

Получаем, редактируем или удаляем пост по id.
```
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)
```
 

Получаем список всех групп.
```
api/v1/groups/ (GET)
```
 

Gолучаем информацию о группе по id.
```
api/v1/groups/{group_id}/ (GET)
```
 

Получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
```
api/v1/posts/{post_id}/comments/ (GET, POST)
```
 

Получаем, редактируем или удаляем комментарий по id у поста с id=post_id
```
 
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)
```
</details>


# Установка
<details><summary>Установка</summary>
 
_На Mac или Linux используем Bash_
_Для Windows PowerShell_

#### Клонируем репозиторий на локальную машину:
```
https://github.com/PythonGun/api_yamdb
git clone git@github.com:PythonGun/api_yamdb.git
```

#### Создаем и активируем виртуальное окружение:
Для Mac или Linux
```
python3 -m venv venv
source venv/bin/activate
```

Для Windows
```
python -m venv venv
source venv/Scripts/activate
```

#### Устанавливаем зависимости:
```
pip install -r requirements.txt
```

#### Запускаем миграции:
```
python manage.py migrate
```

#### Запускаем проект:
```
python manage.py runserver
```
</details>

## Автор
- :white_check_mark: [Баринов Денис](https://github.com/PythonGun)
