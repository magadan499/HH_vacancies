class Vacancy:
    """Класс для работы с вакансиями"""
    list_of_vacancy = []

    def __init__(self, name, city, employer, salary, requirement):
        self.name = name
        self.city = city
        self.employer = employer
        self.salary = salary
        self.requirement = requirement

        Vacancy.list_of_vacancy.append(self)

    def __str__(self):
        return (f"\nНазвание вакансии: {self.name}\n"
                f"Город: {self.city}\n"
                f"Компания: {self.employer}\n"
                f"Заработная плата: {self.salary}\n"
                f"Необходимые навыки: {self.requirement}\n")

    @classmethod
    def transforms_vacancy(cls, vacancies):
        """Преобразует информацию о вакансиях из JSON файла в нужный нам список параметров по вакансиям"""
        for vacancy in vacancies:
            name = vacancy['name']
            city = vacancy['area']['name']
            employer = vacancy['employer']['name']
            try:
                salary = vacancy['salary']['from']
            except TypeError:
                salary = vacancy['salary']
            requirement = vacancy['snippet']['requirement']
            cls(name, city, employer, salary, requirement)

    @staticmethod
    def sorted_salary(vacancies, salary):
        """Сортирует вакансии по минимальной заработной плате"""
        salary_sort = []
        for vacancy in vacancies['items']:
            try:
                if vacancy['salary']['from'] >= salary:
                    salary_sort.append(vacancy)
                if vacancy['salary'] is None:
                    vacancy['salary'] = "Вакансия не найдена"
                if vacancy['salary']['from'] is None:
                    vacancy['salary']['from'] = "Вакансия не найдена"
            except TypeError:
                pass
            if salary == '':
                salary_sort.append(vacancy)
        return salary_sort

    @staticmethod
    def sorted_city(vacancies, city):
        """Сортирует вакансии по названию города"""
        city_sort = []
        for vacancy in vacancies:
            try:
                if city in vacancy['area']['name']:
                    city_sort.append(vacancy)
                if vacancy['area'] is None:
                    vacancy['area'] = "Вакансия не найдена"
                if vacancy['area']['name'] is None:
                    vacancy['area']['name'] = "Вакансия не найдена"
            except TypeError:
                pass
            if city == '':
                city_sort.append(vacancy)
        return city_sort

    @classmethod
    def output_vacancy(cls, vacancies_list) -> None:
        """Выводит отсортированные вакансии"""
        for vacancy in vacancies_list:
            print(vacancy)
