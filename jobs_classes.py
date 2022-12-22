
class Vacancy(list):
    __all = []
    i = 0

    __slots__ = ('name', 'href', 'salary')

    def __init__(self, name, href, salary):
        self.name = name
        self.href = href
        # self.description = description
        self.salary = salary
        self.__all.append(self)

    def return__all(self):
        return self.__all

    #функция для добавления экземпляров в один список
    def __setitem__(self):
        self.__all.append(self)

    def __repr__(self):
        return f'Название: {self.name}, ссылка: {self.href}, зп: {self.salary}'

    # проверка данных
    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        return other if isinstance(other, int) else other.salary

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.salary == int(sc)

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.salary < int(sc)

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.salary > int(sc)

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.salary <= int(sc)

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.salary >= int(sc)

    def __next__(self):
        if self.i < len(self.__all):
            current = self.__all
            self.i += 1
            return current
        else:
            raise StopIteration

    def __iter__(self):
        return iter(self.__all)

    def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
        state = {"name": self.name, "href": self.href, "salary": self.salary}
        return state


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        return



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __repr__(self):
        return f'HH: {self.name}, ссылка: {self.href}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __repr__(self):
        return f'HH: {self.name}, ссылка: {self.href}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    return sorted(vacancies, reverse=True)


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    new = sorting(vacancies)[0:int(top_count)]
    return new

