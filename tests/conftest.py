import pytest

from config import TEST_VACANCIES_PATH_JSON, TEST_VACANCIES_PATH_TXT
from src.json_saver import JSONSaver
from src.txt_saver import TXTSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy("Продавец-кассир (Центральный район)", "https://hh.ru/vacancy/84107331",
                   49_000, 57_000, "Ангарск",
                   "Опыт работы не важен", "Расширенные программы денежных надбавок и премий")


@pytest.fixture()
def vacancy2():
    return Vacancy("Продавец-кассир (Центральный район)", "https://hh.ru/vacancy/84107331",
                   39_000, 47_000, "Ангарск",
                   "Опыт работы не важен", "Расширенные программы денежных надбавок и премий")


@pytest.fixture()
def json_saver():
    return JSONSaver(filename=TEST_VACANCIES_PATH_JSON)


@pytest.fixture()
def txt_saver():
    return TXTSaver(filename=TEST_VACANCIES_PATH_TXT)
