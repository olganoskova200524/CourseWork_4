def test_vacancy_init(vacancy1):
    """
    Тест инициализации и корректность работы атрибутов класса Vacancies
    """

    assert vacancy1.name == "Продавец-кассир (Центральный район)"
    assert vacancy1.alternate_url == "https://hh.ru/vacancy/84107331"
    assert vacancy1.salary_from == 49_000
    assert vacancy1.salary_to == 57_000
    assert vacancy1.area_name == "Ангарск"
    assert vacancy1.requirement == "Опыт работы не важен"
    assert vacancy1.responsibility == "Расширенные программы денежных надбавок и премий"


def test_vacancy_str(vacancy1):
    """
    Проверка строкового представления вакансии
    """

    assert str(vacancy1) == ("Наименование вакансии: Продавец-кассир (Центральный район)\n"
                             "Ссылка на вакансию: https://hh.ru/vacancy/84107331\n"
                             "Зарплата: от 49000 до 57000\n"
                             "Место работы: Ангарск\n"
                             "Краткое описание: Опыт работы не важен\n"
                             "Расширенные программы денежных надбавок и премий\n")


def test_vacancy_lt(vacancy1, vacancy2):
    """
    Проверка метода сравнения от большего к меньшему
    """

    assert vacancy2 < vacancy1
    if vacancy1 > vacancy2:
        assert ValueError


def test_vacancy_from_hh_dict(vacancy1):
    """
    Проверка воврата экземпляра класса в виде списка
    """

    assert (
        "Наименование вакансии: Продавец-кассир (Центральный район),"
        "Ссылка на вакансию: https://hh.ru/vacancy/84107331"
        "Зарплата: от 49000 до 57000,"
        "Место работы: Ангарск"
        "Краткое описание: Опыт работы не важен"
        "Расширенные программы денежных надбавок и премий"
    )


def test_vacancy_to_dict(vacancy1):
    """
    Проверка, что метод возвращает вакансию в виде словаря """

    assert {
        "name": "Продавец-кассир (Центральный район)",
        "alternate_url": "https://hh.ru/vacancy/84107331",
        "salary_from": 49000,
        "salary_to": 57000,
        "area_name": "Ангарск",
        "requirement": "Опыт работы не важен",
        "responsibility": "Расширенные программы денежных надбавок и премий"
    }
