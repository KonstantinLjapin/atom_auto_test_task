### Требования
- linux(Ubuntu)
- docker compose
- python3.11
### Быстрый старт
- git clone {repositories} / колонируем репозиторий
- pip install --upgrade pip / для отладки
- pip install pip install -r requirements.txt 
- sudo ./start_alaska.sh / запуск
### Описание задачи
докер-образ: azshoo/alaska:1.0
В образе находится CRUD сервис, информацию о API можно получить по ручке /info Задача:
написать стратегию тестирования этого сервиса, написать тесты в любом формате, 
автоматизировать выборочно несколько тестов с использованием python + pytest


### Описание реализации
Проведён анализ эндпоинтов подготовлен скрипт запускающий образ с тестируемым контейнером результат тестирования
pytest записывается в файл result.txt. Используется позитивная и негативная методика тестирования также запускается 
небольшой нагрузочный тест. Выевленые недостатки в контейнере на негативном тестирование.

### Эндпоинты
_ http://0.0.0.0:8091/info / GET информация
- http://0.0.0.0:8091/bear / POST,GET, DELETE
- http://0.0.0.0:8091/bear:id / GET, DELETE, PUT
### Тестирование
- для шаловливых ручек есть коллекция для postman

 PyTest
- TestPositive::test_info 
- TestPositive::test_bears 
- TestPositive::test_post_bear
- TestPositive::test_put_bear
- TestPositive::test_delete_bear
- TestPositive::test_delete_all_bear
- TestNegative::test_info
- TestNegative::test_bears
- TestNegative::test_post_bear 
- TestNegative::test_put_bear 
- TestNegative::test_delete_bear 
- TestNegative::test_delete_all_bear
- TestBrake::test_info / нагрузочный
