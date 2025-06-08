import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass

    @abstractmethod
    def connect_api(self, params: dict) -> list[dict]:
        pass




class HeadHunterAPI(AbstractAPI):
    """Класс для получения вакансий с hh.ru по ключевому слову."""
    __slots__ = ('__url',)

    def __init__(self, url = "https://api.hh.ru/vacancies"):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_url(self, new_url):
        self.__url = new_url

    def __connect_api(self, params: dict) -> dict:
        """
        Выполняет запрос к API hh.ru и возвращает распаршенный JSON.
        """
        headers = {
            "User-Agent": "HH-User-Agent"
        }
        response = requests.get(self.__url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Возвращает список вакансий с hh.ru по ключевому слову.
        """
        params = {
            "text": keyword,
            "per_page": 100
        }
        data = self.__connect_api(params)
        return data.get("items", [])