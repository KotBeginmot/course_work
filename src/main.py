from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancies import HeadHunterAPI, JsonSaver, SuperJobAPI, Vacancies

JSON_FILE = "vacancy.json"

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_save = JsonSaver(JSON_FILE)
vacancy_1 = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", "50 000-150 000 руб.", "Требования: опыт "
                                                                                                    "работы от 3 "
                                                                                                    "лет...")


def user_interaction():
    platform = ["HeadHunter", "SuperJob"]
    print(f'Поиск вакансий на платформах {platform[0]} и {platform[1]}')
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    hh_api.get_vacancies(search_query)
    superjob_api.get_vacancies(search_query)
    filtered_vacancies = filter_vacancies(hh_api.hh, superjob_api.sj, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    vacancies = []
    for api in (hh_api, superjob_api):
        vacancies.extend(api.get_formatted_vacancies())
    json_save.save_vacancies(vacancies)

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
