import pytest
from src.working_with_vacancy import Vacancy


def test_sorted_salary():
    """Проверка сортировки вакансии по минимальной заработной плате"""
    vacancies = {"items": [{'name': 'Военнослужащий', 'salary': {'from': 40000}},
                 {'name': 'Разработчик', 'salary': {'from': 80000}},
                 {'name': 'Системный администратор', 'salary': None}]}
    filter_vacancy = Vacancy.sorted_salary(vacancies, 55000)
    assert len(filter_vacancy) == 1
    assert filter_vacancy[0]['name'] == 'Разработчик'


def test_sorted_city():
    """Проверка сортировки вакансии по названию города"""
    vacancies = [{'name': 'Разработчик', 'area': {'name': 'Moscow'}},
                        {'name': 'Системный администратор', 'area': {'name': 'Saint Petersburg'}},
                        {'name': 'Военнослужащий', 'area': None}]
    filter_vacancy = Vacancy.sorted_city(vacancies, 'Moscow')
    assert len(filter_vacancy) == 1
    assert filter_vacancy[0]['name'] == 'Разработчик'
