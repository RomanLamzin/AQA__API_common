from utils.api import Google_maps_api
from utils.checking import Checking
import allure

"""Создание, изменение и удаление новой локации"""

@allure.epic("Test create place")
class Test_create_place():
    """Класс содержащий тест по работе с локацией"""

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()  # вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")           # получения place_id для метода GET
        Checking.check_status_code(result_post, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')
        print("*************************************")


        print("Метод GET")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        print("*************************************")

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)  # вызов метода по проверке статус-кода
        print("*************************************")

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        print("*************************************")

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)  # вызов метода по проверке статус-кода
        print("*************************************")

        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')
        print("*************************************")










# python -m pytest -s -v
# python -m pytest --alluredir=test_results/ tests/test_google_maps_api.py