import allure
import requests

from utils.logger import Logger

"""Список HTTP методов"""


class Http_methods:
    headers = {'Content-type': 'application/json'}  # Заголовки нашего проекта
    cookie = ""  # Куки нашего проекта

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, 'GET')
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, 'POST')
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, 'PUT')
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, 'DELETE')
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

