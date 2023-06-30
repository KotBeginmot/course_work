from abc import ABC, abstractmethod
from http import HTTPStatus

import requests




class VacanciesAPI(ABC):
    pass

class HeadHunterAPI(VacanciesAPI):
"""Класс для API с HH.ru"""
    api_hh = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.hh = None

    def get_vacancies(self, options: str):
        """Функция по выбору заданных профессий с HH.ru"""
        answer = requests.get(f"{HeadHunterAPI.api_hh}{options}")
        if not answer.status == HTTPStatus.OK:
            return f"Ошибка {answer.status}"

        self.hh = answer.json()
        return self.hh

class SuperJobAPI(VacanciesAPI):
    """Функция по выбору заданных профессий с SJ.ru"""
    api_sj = "	https://api.superjob.ru/2.0/vacancies/"

    def __init__(self):
        self.sj = None

    def get_vacancies(self, params: str):
        """Функция по выбору заданных профессий с HH.ru"""
        headers = {"X-Api-App-Id": 'v3.r.137647469.a54884c0bd65321ee0b9e549b91cd7c806a3ee2b.3be8bc0f9da9528233272a060365f321f20ec1d3'}
        params = {"keyword": "Python"}

        answer = requests.get(SuperJobAPI.api_sj, headers=headers, params=params)
        if not answer.status == HTTPStatus.OK:
            return f"Ошибка {answer.status}"

        self.sj = answer.json()
        return self.sj

