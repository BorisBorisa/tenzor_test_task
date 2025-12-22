## Описание

Репозиторий содержит реализацию [тестового задания](https://github.com/BorisBorisa/tenzor_test_task/blob/master/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20(%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5).pdf) по автоматизации UI тестирования.


## Начало работы

### Клонирование репозитория

```
git clone https://github.com/BorisBorisa/tenzor_test_task.git
cd tenzor_test_task
```

### Создание виртуального окружения
#### Linux / MacOS
```
python3 -m venv venv
source venv/bin/activate
```
#### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей
```
pip install -r requirements.txt
```
### Запуск тестов с генерацией результатов Allure
```
python -m pytest --alluredir=./allure-results
```

### Генерация отчета Allure
```
allure serve allure-results
```
*Для генерации отчета Allure необходима [Java](https://www.oracle.com/java/technologies/downloads/#java11) (как минимум JRE) и [Allure CLI](https://allurereport.org/docs/v2/install/)*

Эта команда откроет отчет Allure в вашем браузере по умолчанию.
