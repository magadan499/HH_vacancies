from abc import ABC
import json
from config import JSON_VACANCY


class Saver(ABC):
    """Абстрактный класс для работы с Json файлом"""
    def add_vacancy(self, data):
        """Сохраняет вакансии"""
        pass

    def delete_vacancy_json(self):
        """Метод очистки файла Json"""
        pass

    def read_vacancy(self):
        """Метод для чтения файла"""
        pass


class SaveVacancy(Saver):
    """Класс сохраняет информацию о вакансиях в файл JSON"""

    def add_vacancy(self, vacancies):
        """Сохраняет вакансии в json файл"""
        with open(JSON_VACANCY, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=5, ensure_ascii=False)

    def read_vacancy(self):
        """Читает json файл c вакансиями"""
        with open(JSON_VACANCY, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def delete_vacancy_json(self):
        """Очищает json файл с вакансиями"""
        pass
