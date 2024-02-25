from abc import ABC, abstractmethod
import requests


class ApiVacancy(ABC):
    """Абстрактный класс для работы с API и вакансиями"""
    @abstractmethod
    def get_vacancy(self, search_query, top_n):
        pass


class VacancyJson(ApiVacancy):
    """Класс для работы с API (hh.ru) и получения вакансий в формате Json"""
    def get_vacancy(self, search_query, top_n):
        """Получение вакансий в формате JSON"""
        data = requests.get(f"https://api.hh.ru/vacancies",
                            params={'text': f'{search_query}', 'area': 113, 'per_page': f'{top_n}'}).json()
        return data
