import json
from config import JSON_VACANCY


class SaveVacancy:
    """Класс сохраняет информацию о вакансиях в файл JSON"""
    @staticmethod
    def add_vacancy(vacancies):
        """Сохраняет вакансии в json файл"""
        with open(JSON_VACANCY, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=5, ensure_ascii=False)

    @staticmethod
    def read_vacancy():
        """Читает json файл c вакансиями"""
        with open(JSON_VACANCY, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def delete_vacancy_json():
        """Очищает json файл с вакансиями"""
        pass
