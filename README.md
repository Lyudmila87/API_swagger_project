
# _Проект к практикуму SDET: API-тесты_

В проекте использованы:
* Python - requests
* Python – pydantic
* Фреймворк Pytest
* Реализовано формирование отчетов Allure
* Реализован запуск в системе CI/CD
* Реализован многопоточный запуск

Версия Python 3.11

____
Установка и запуск:
1. Воспользовать инструкцией и развернуть проект: `https://github.com/sun6r0/test-service.git`
2. Склонировать репозиторий: `git clone https://github.com/Lyudmila87/API_swagger_project.git`
3. Перейти в директорию проекта
4. Создать виртуальное окружение `python -m venv venv`
5. Активировать окружение: `venv\Scripts\activate`
6. Установить зависимости `pip install -r requirements.txt`
7. Запустить тесты `pytest --alluredir=allure_report -v`
   * Команда для многопоточного запуска `pytest --alluredir=allure_report -v -n 2`
8. Запустить allure-отчет `allure serve allure_report`
