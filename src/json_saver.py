import json

from src.saver import Saver


class JSONSaver(Saver):
    """
    Класс для записи в json-файл
    """

    def __init__(self, filename):
        """Конструктор класса
        """

        super().__init__(filename)

    def write_data(self, vacancies):
        """
        Запись данных в json фаил
        """

        data = self.get_data()
        data.extend(vacancies)

        with open(self.filename, "w", encoding="utf-8") as file:
            return json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """
        Получение данных json фаил
        """

        try:
            return json.load(open(self.filename))
        except FileNotFoundError:
            return []

    def del_data(self):
        """
        Удаление данных из json файла
        """

        with open(self.filename, "w", encoding="utf-8") as file:
            return json.dump([], file, ensure_ascii=False, indent=4)
