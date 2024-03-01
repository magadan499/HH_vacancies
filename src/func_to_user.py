from src.working_with_vacancy import Vacancy
from src.abstract_api_vacancy import VacancyJson
from src.save_vacancy_json import SaveVacancy


def user_interaction():
    """Запрашивает необходимые данные от пользователя по вакансиям"""
    search_query = str(input('Введите название вакансии: '))
    top_n = int(input('Введите количество вакансий: '))
    city = str(input('Введите название города: '))
    salary = int(input('Введите минимальную заработную плату: '))
    api_hh = VacancyJson()
    vacancy_hh = api_hh.get_vacancy(search_query, top_n)
    json_hh = SaveVacancy()
    json_hh.add_vacancy(vacancy_hh)
    data = json_hh.read_vacancy()
    salary_sort = Vacancy.sorted_salary(data, salary)
    city_sort = Vacancy.sorted_city(salary_sort, city)
    Vacancy.transforms_vacancy(city_sort)
    if not Vacancy.list_of_vacancy:
        print('\nПодходящих вакансий не найдено')
    else:
        print('\nПодходящие вакансии: ')
        Vacancy.output_vacancy(Vacancy.list_of_vacancy)
