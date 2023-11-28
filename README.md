# Book Test Task

## Сборка проекта

* Создайте директорию для проекта (например: D:/book_test_task)
* Откройте консольную программу и перейдите в директорию проекта (например: PowerShell и 'cd D:/book_test_task')
* Клонируйте проект: git clone https://github.com/amiddio/book_test_task.git .
* В директории '/src' создайте '.env' файл. За образец нужно взять '.env.example'. В нем укажите значения для отправки email-а.
* Запустите Docker
* С корня ('D:/book_test_task') запустите: docker-compose build
* И после: docker-compose up
* Проект должен успешно запуститься, и будет готов к тестированию

## База Данных

Можно посмотреть БД перейдя в браузере на: http://localhost:8888/

* System: MySQL
* Server: db
* Username: book_user
* Password: password
* Database: book_db

## Unittests

Для запуска юниттестов необходимо:

* С корня ('D:/book_test_task') проекта запустите еще одну консоль (например: PowerShell)
* Далее команду: docker exec -it book_test_task-db-1 mysql -uroot -p
* Введите пароль: password
* После: GRANT ALL PRIVILEGES ON *.* TO 'book_user'@'%';
* И: exit
* Запуск юниттестов: docker-compose run --rm  web-app sh -c "python manage.py test"

Примечание: на данный момент юниттестами покрыты эндпойнты управления книгами

## Тестирование проекта

Для тестирования удобно использовать Postman

### Эндпойнты для управления книгами

* добавление книги POST: http://127.0.0.1:8000/api/v1/books/
* список книг GET: http://127.0.0.1:8000/api/v1/books/
* книга GET: http://127.0.0.1:8000/api/v1/books/[BOOK_ID]/
* обновление книги PUT: http://127.0.0.1:8000/api/v1/books/[BOOK_ID]/
* удаление книги DELETE: http://127.0.0.1:8000/api/v1/books/[BOOK_ID]/

### Эндпойнт регистрации пользователя

* http://127.0.0.1:8000/api/v1/customer_register

## Скриншоты демонстрирующие работу проекта

### Добавление книги
![Screenshot_1](/screenshots/Screenshot_1.png)

### Список книг
![Screenshot_1](/screenshots/Screenshot_2.png)

### Книга
![Screenshot_1](/screenshots/Screenshot_3.png)

### Изменение книги
![Screenshot_1](/screenshots/Screenshot_4.png)

### Удаление книги
![Screenshot_1](/screenshots/Screenshot_5.png)

### Добавление пользователя
![Screenshot_1](/screenshots/Screenshot_9.png)
![Screenshot_1](/screenshots/Screenshot_6.png)
![Screenshot_1](/screenshots/Screenshot_7.png)

### Юниттесты
![Screenshot_1](/screenshots/Screenshot_8.png)

### Repository
![Screenshot_1](/screenshots/Screenshot_10.png)
