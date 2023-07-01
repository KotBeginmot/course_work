## Требования к реализации

1. Создать абстрактный класс для работы с API сайтов с вакансиями. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии.
2. Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех) Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
3. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.
4. Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. Самостоятельно придумать сценарии и возможности взаимодействия с пользователем. Например, позволять пользователю указать, с каких платформ он хочет получить вакансии, ввести поисковый запрос, получить топ N вакансий по зарплате, получить вакансии в отсортированном виде, получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т. п.
5. Объединить все классы и функции в единую программу.
