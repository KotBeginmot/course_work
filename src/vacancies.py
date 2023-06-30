class Vacansies:
    def __init__(self, name, url, salary, skills):

        self.name = name
        self.url = url
        self.salary = salary
        self.skills = skills

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

