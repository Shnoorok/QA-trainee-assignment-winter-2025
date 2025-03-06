# Решение тестового задания для стажёра QA-направления (зимняя волна 2025)

**Задание 1**

Описание Задания

Необходимо изучить перечислите все имеющиеся баги а так же укажить приоритет (high, medium, low) для изображения по ссылке: 
https://github.com/user-attachments/assets/a8c18dc6-bd16-4ba0-b152-2762922d542c

Решение для задания 1 находится в фале Task_1.md в корневом каталоге по ссылке: https://github.com/Shnoorok/QA-trainee-assignment-winter-2025/blob/main/Task_1.md

**Задание 2.1**

Описание Задания


Необходимо составьте тест-кейсы для проверки api микросервиса
Оформить решение в файле TESTCASES.md
Автоматизировать написанные тест-кейсы 
В автоматизированных тест-кейсах необходимо проверять результат
Провести все автоматизированные тесты
Если в результате тестирования найдены баги, необходимо составить баг-репорт в файле BUGS.md

**Решение:**

Для выполнения нужно воспользоваться интерпритатором Python такие как Visual stuio, Pycharm etc.

Скопируйте репозиторий:

git clone https://github.com/your-username/QA-trainee-assignment-winter-2025.git

cd QA-trainee-assignment-winter-2025

**Создайте виртуальное окружение:**

python -m venv venv
source venv/bin/activate  Для Linux/MacOS
venv\Scripts\activate     Для Windows

**Установите зависимости:**

pip install -r requirements.txt

**Для запуска тестов выполните команду в терминале вашего интерпритатора:**

pytest tests/test_api.py

**Для вывода подробной информации о тестах:**

pytest -v tests/test_api.py

**Логирование**

Логи тестов сохраняются в файл test_logs.log в корневой папке проекта. Логи содержат информацию о запросах, ответах сервера и результатах выполнения тестов.

**Пример содержимого логов:**

2025-02-16 22:56:10,659 - INFO - Отправка GET-запроса на https://qa-internship.avito.com/api/1/statistic/0cd4183f-a699-4486-83f8-b513dfde477a
2025-02-16 22:56:10,718 - INFO - Ответ сервера: 200, [{"contacts":3,"likes":246,"viewCount":258}]

2025-02-16 23:04:06,486 - INFO - Отправка POST-запроса на https://qa-internship.avito.com/api/1/item с данными: {'sellerID': 123456, 'name': 'Test Item', 'price': 100, 'statistics': {'contacts': 3, 'likes': 123, 'viewCount': 12}}
2025-02-16 23:04:06,621 - INFO - Ответ сервера: 200, {"status":"Сохранили объявление - 3de194f0-a7e1-424a-99f9-ab7f100b6886"}

**Баги:**

Обнаруженные в процессе тестирования баги описаны в файле BUGS.md, ссылка: https://github.com/Shnoorok/QA-trainee-assignment-winter-2025/blob/main/BUGS.md

