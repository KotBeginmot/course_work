from abc import ABC, abstractmethod
import json

class Json(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

class JsonSaver(Json):
    def __init__(self, filename):
        self.filename = filename

    def save_vacancies(self, vacancies):
        with open(self.filename, "w", encoding="utf8") as json_file:
            json.dump(vacancies, fp=json_file)

    def load_vacancies(self):
        with open(self.filename, "r", encoding="utf8") as json_file:
            vacancies = json.load(fp=son_file)
        return vacancies

    def delete_vacancies(self):
        with open(self.filename, "w", encoding="utf8") as json_file:
            json.dump([], fp=json_file)