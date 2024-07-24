def test_write_data(json_saver):
    """
    Тест на добавление вакансии в json.file
    """

    json_saver.write_data(
        [
            {
                "name": "Водитель с л/а (замена батарей на электросамокатах)",
                "alternate_url": "https://hh.ru/vacancy/98568415",
                "salary_from": 600000,
                "salary_to": 1200000,
                "area_name": "Алматы",
                "requirement": "Ответственность.",
                "responsibility": "Замена батарей в городе на электросамокатах. "
                                  "Проверка состояния самокатов в городе. "
                                  "Телефон на базе Android. Чистые счета без арестов(по..."
            }
        ]
    )


def test_get_data(json_saver):
    """
    Проверяем, что в файле лежит одна вакансия
    """

    assert len(json_saver.get_data()) == 1


def test_del_data(json_saver):
    """
    Проверяем, что файл пустой после удаления данных
    """

    assert json_saver.del_data() is None
