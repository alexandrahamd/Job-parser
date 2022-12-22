from class_connector import Connector
from classes import Superjob, HH
from utils import *
from jobs_classes import *


if __name__ == '__main__':
    sj = Superjob()
    hh = HH()
    search_word = input('Введите слово поиска: ')
    vacancies_count = int(input('Введите колличество вакансий с каждого сайта: '))
    top_count = input('Введите колличество топ вакансий: ')
    result_sj = sj.get_request(search_word, vacancies_count)    #запрос на сайте
    result_hh = hh.get_request(search_word, vacancies_count)
    connector_sj = Connector('df_sj.json')  # создание экземпляра
    connector_hh = Connector('df_hh.json')
    connector_sj.insert(result_sj)   #сохранение запроса в файле
    connector_hh.insert(result_hh)
    res_hh = list(read_file_hh('df_hh.json'))   #чтение файла
    res_sj = list(read_file_js('df_sj.json'))
    vacancies_hh = [HHVacancy(i['name'], i['href'], i['salary']) for i in res_hh]   #создание экземпляров класса из файла
    vacancies_sj = [SJVacancy(i['name'], i['href'], i['salary']) for i in res_sj]
    print(f"С сайта SJ {vacancies_sj[1].get_count_of_vacancy('df_sj.json')} вакансий")    # получение колличества вакансий из файла
    a = Vacancy('0', '0', '0')
    _all = Vacancy.return__all(a)  # все вакансии вместе
    sorting__all = sorting(Vacancy.return__all(a))  # сортировка всех вакансий
    top_vacancies = get_top(sorting__all, 5)   # топ вакансий
    iterator = iter(top_vacancies)         #итератор
    insert(top_vacancies)       #добавление результата в файл
    while True:    #вывод результата на экран
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break
