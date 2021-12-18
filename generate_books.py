import conf
import random
from faker import Faker


def pk_inc(start_value: int = 1) -> int:
    """инкримент pk"""

    pk = start_value
    while True:
        yield pk
        pk += 1


def get_title() -> str:
    """выдача названия книги из файла"""

    title_list = []
    with open('books.txt', 'rt', encoding='utf-8') as t_f:
       for title in t_f:
           title_list.append(title.rstrip())

    while True:
        yield ''.join(random.choices(title_list))


def get_number(wtw: str = 'year') -> int:
    """генерация случайного числа (год или кол-во страниц)"""

    if wtw == 'year':
        return random.randint(1700, 2021)
    elif wtw == 'pages':
        return random.randint(1, 10000)
    else:
        return 0


def get_isbin() -> str:
    """генерация isbin"""

    fake = Faker()
    return fake.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')


def get_float(wtw: str = 'rating') -> float:
    """получение рейтинга или цены"""

    if wtw == 'rating':
        return random.uniform(0.0, 6.0)
    elif wtw == 'price':
        return random.uniform(0.1, 10000)
    else:
        return 0.0


def get_author() -> list[str]:
    """получение списка авторов"""

    fake = Faker(locale="ru_RU")
    i = random.randint(1, 3)
    result = list(fake.name() for _ in range(i))
    return result


def dit_creator(count: int = 5) -> list:
    """сборка словаря"""

    pk = pk_inc()
    title = get_title()
    result = []
    for _ in range(count):
        dict_res = {"model": conf.MODEL,
                      'pk': next(pk),
                      'fields': {
                          "title": next(title),
                          "year": get_number('year'),
                          "pages": get_number('pages'),
                          "isbn13": get_isbin(),
                          "rating": f'{get_float("rating"):.1f}',
                          "price": f'{get_float("price"):.2f}',
                          "author": get_author()
                         }
                    }
        result.append(dict_res)
    return result
