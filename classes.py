from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    __per_page = 20
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    __per_page = 20
    __url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_word, page):
        response = requests.get(f'{self.__url}?text={search_word}&page={page}')

        if response.status_code == 200:
            return response.json()
        return None

    def get_request(self, search_word, vacancies_count):
        page = 0
        result = []
        while self.__per_page * page < vacancies_count:
            tmp_result = self.get_vacancies(search_word, page)
            if tmp_result:
                result += tmp_result.get('items')
                page += 1
            else:
                break
        return result


class Superjob(Engine):
    __per_page = 20
    __url = 'https://api.superjob.ru/2.0/vacancies/search/'
    __key = 'v3.r.137220942.b0c97142781dbc5ff05363047765c12f96331dd2.26c8a5a418e12a874f523c729ec16883553d38a7'

    def get_vacancies(self, search_word, vacancies_count):
        headers = {
            'X-Api-App-Id': self.__key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.get(url=f'{self.__url}?keywords={search_word}', headers=headers)
        if response.status_code == 200:
            return response.json()
        return None


    def get_request(self, search_word, vacancies_count):
        page = 0
        result = []
        self.get_vacancies(search_word, vacancies_count)
        while self.__per_page * page < vacancies_count:
            tmp_result = self.get_vacancies(search_word, page)
            if tmp_result:
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        return result




