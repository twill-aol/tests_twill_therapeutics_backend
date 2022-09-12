
import pytest
import requests


class TestFirstAPI:
    names = [
        ("Mike"),
        ("Olga"),
        ()
    ] # добавили словарь с кортежами, содержащие имена

    @pytest.mark.parametrize('name', names) # довесили pytest-вое переопределение (как функциональная дообёртка) функции-тесту, которая добавляет новые возможности (прогонка значений указанных переменных). Переменной 'name' в ней будут подставляться значения из нашего словаря names
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        # удалили прошлое конкретизированное установление имени. Остальное остаётся прежним
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no filed 'answer' in response"

        if len(name) > 0:
            expected_response_text = f"Hello, {name}"
        else:
            expected_response_text = "Hello, someone"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text , "Actual text in the response is not correct"
