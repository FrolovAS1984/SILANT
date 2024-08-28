## Описание проекта

Проект "Silant" состоит из двух частей: backend и frontend. 
Backend реализован с использованием Django и Django REST framework, frontend построен на React.

## Установка и запуск проекта

### 1. Клонирование репозитория

Клонируйте репозиторий на свой локальный компьютер:

https://github.com/FrolovAS1984/SILANT.git


### 2. Настройка backend

-Перейдите в папку backend

    cd .\Backend\

-Создайте и активируйте виртуальное окружение

-Установите зависимости:

    pip install -r requirements.txt

-Перейдите в папку silant

    cd .\silant\

-Выполните миграции базы данных:

    python manage.py migrate

-Создайте суперпользователя:

    python manage.py createsuperuser


-Запустите сервер разработки:

    python manage.py runserver


### 3. Настройка frontend

-Перейдите в папку frontend:

    cd .\Frontend\

-Установите зависимости:

    npm install

-Для разработки запустите сервер разработки:

    npm run dev

### API Документация

Документация по API доступна по адресу http://localhost:8000/api/swagger/ после запуска сервера backend.


### Приложение открывается по адресу http://localhost:5173/


### Логины для авторизации

Менеджер:

логин: manager
пароль: z55-xba-eHn-fPY
_____________________________
Клиенты:

ИП Трудников С.В.
логин: client1
пароль: FvY-sEr-8ZZ-An7

ООО "ФПК21"
логин: client2
пароль: fnq-NsM-2gh-ruP

ООО "МНС77"
логин: client3
пароль: jNj8Bj4Rzxyj6PR

ООО "Ранский ЛПХ"
логин: client4
пароль: 2f8xjQjjaHv8Caz

ООО "Комплект-Поставка"
логин: client5
пароль: unYZh48qV3RayPe

ООО "РМК"
логин: client6
пароль: 26s9hTAx8VSZqER

АО "Зандер"
логин: client7
пароль: j2FUWehygCVYWLe
_______________________________
Сервисные компании:

ООО Промышленная техника
логин: service1
пароль: d24-Mdk-5hF-vP2

ООО Силант
логин: service2
пароль: p27-6eC-Zh6-dk6

ООО ФНС
логин: service3
пароль: xiSAg3wKD94SE7P

