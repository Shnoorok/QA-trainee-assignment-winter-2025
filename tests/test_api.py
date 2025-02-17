import requests
import pytest
import logging
import os

# настройки логирования в файл test_logs.log в папку tests
log_file_path = os.path.join(os.path.dirname(__file__), "test_logs.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

BASE_URL = "https://qa-internship.avito.com"

# Тест-кейс 1.1.1: Успешное создание объявления с корректными данными
def test_create_item_success():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "Сохранили объявление" in response.text

# Тест-кейс 1.1.2: Создание объявления с минимальными данными (только обязательные поля)
def test_create_item_minimal_data():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": 100
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "Сохранили объявление" in response.text

# Тест-кейс 1.2.1: Попытка создания объявления без обязательного поля (sellerID)
def test_create_item_missing_seller_id():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 1.2.2: Попытка создания объявления с некорректным типом данных (строка вместо числа в поле price)
def test_create_item_invalid_price_type():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": "invalid_price",  # Некорректный тип данных
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 1.2.3: Попытка создания объявления с пустым телом запроса
def test_create_item_empty_body():
    url = f"{BASE_URL}/api/1/item"
    payload = {}
    logger.info(f"Отправка POST-запроса на {url} с пустым телом запроса")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 1.2.4: Попытка создания объявления с отрицательным значением price
def test_create_item_negative_price():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": -100,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 1.2.5: Попытка создания объявления с очень длинным значением поля name
def test_create_item_long_name():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "A" * 1000,  # Очень длинное имя
        "price": 100,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 2.1.1: Успешное получение объявления по существующему id
def test_get_item_by_id_success():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    url = f"{BASE_URL}/api/1/item/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "id" in response.json()[0]

# Тест-кейс 2.1.2: Получение объявления с проверкой всех полей
def test_get_item_check_all_fields():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    url = f"{BASE_URL}/api/1/item/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    item = response.json()[0]
    assert "id" in item
    assert "sellerId" in item
    assert "name" in item
    assert "price" in item
    assert "statistics" in item
    assert "createdAt" in item

# Тест-кейс 2.2.1: Попытка получения объявления по несуществующему id
def test_get_item_by_nonexistent_id():
    item_id = "non-existent-id"
    url = f"{BASE_URL}/api/1/item/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 404

# Тест-кейс 2.2.2: Попытка получения объявления с некорректным форматом id
def test_get_item_by_invalid_id_format():
    item_id = "invalid_id_format"
    url = f"{BASE_URL}/api/1/item/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 2.2.3: Попытка получения объявления с пустым id
def test_get_item_by_empty_id():
    item_id = ""
    url = f"{BASE_URL}/api/1/item/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 3.1.1: Успешное получение всех объявлений по существующему sellerID
def test_get_items_by_seller_id_success():
    seller_id = 1234345231
    url = f"{BASE_URL}/api/1/{seller_id}/item"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тест-кейс 3.2.1: Попытка получения объявлений с некорректным форматом sellerID
def test_get_items_by_invalid_seller_id_format():
    seller_id = "invalid_seller_id"
    url = f"{BASE_URL}/api/1/{seller_id}/item"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 3.2.2: Попытка получения объявлений с отрицательным значением sellerID
def test_get_items_by_negative_seller_id():
    seller_id = -123456
    url = f"{BASE_URL}/api/1/{seller_id}/item"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 4.1.1: Успешное получение статистики по существующему id
def test_get_statistic_by_id_success():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    url = f"{BASE_URL}/api/1/statistic/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "likes" in response.json()[0]

# Тест-кейс 4.1.2: Получение статистики с проверкой всех полей
def test_get_statistic_check_all_fields():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    url = f"{BASE_URL}/api/1/statistic/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    statistic = response.json()[0]
    assert "likes" in statistic
    assert "viewCount" in statistic
    assert "contacts" in statistic

# Тест-кейс 4.2.1: Попытка получения статистики по несуществующему id
def test_get_statistic_by_nonexistent_id():
    item_id = "non-existent-id"
    url = f"{BASE_URL}/api/1/statistic/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 404

# Тест-кейс 4.2.2: Попытка получения статистики с некорректным форматом id
def test_get_statistic_by_invalid_id_format():
    item_id = "invalid_id_format"
    url = f"{BASE_URL}/api/1/statistic/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 4.2.3: Попытка получения статистики с пустым id
def test_get_statistic_by_empty_id():
    item_id = ""
    url = f"{BASE_URL}/api/1/statistic/{item_id}"
    logger.info(f"Отправка GET-запроса на {url}")
    response = requests.get(url)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 400

# Тест-кейс 5.1.1: Создание объявления с минимальным значением price
def test_create_item_min_price():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": 0,  # Минимальное значение
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "Сохранили объявление" in response.text

# Тест-кейс 5.1.2: Создание объявления с максимальным значением price
def test_create_item_max_price():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerID": 123456,
        "name": "Test Item",
        "price": 999999999,  # Максимальное значение
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    logger.info(f"Отправка POST-запроса на {url} с данными: {payload}")
    response = requests.post(url, json=payload)
    logger.info(f"Ответ сервера: {response.status_code}, {response.text}")
    assert response.status_code == 200
    assert "Сохранили объявление" in response.text

# Запуск тестов
if __name__ == "__main__":
    pytest.main()