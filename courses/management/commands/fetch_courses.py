from django.core.management.base import BaseCommand
from courses.models import Course, Lesson


class Command(BaseCommand):
    help = 'Загрузка курсов'

    def handle(self, *args, **kwargs):
        self.stdout.write('Загружаем курсы...')

        data = [
            {
                'course': {
                    'stepik_id': 1001,
                    'title': 'Python для начинающих',
                    'description': 'Полный курс Python с нуля. Переменные, циклы, функции, ООП.',
                    'language': 'python', 'level': 'beginner', 'price': 0,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Введение в Python', 'content': 'Python — популярный язык программирования. Установка и первая программа.', 'order': 1, 'quiz_question': 'Как вывести текст в Python?', 'quiz_answer': 'print', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Переменные и типы данных', 'content': 'int, float, str, bool, list, dict — основные типы данных Python.', 'order': 2, 'quiz_question': 'Тип целого числа в Python?', 'quiz_answer': 'int', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Условия if/else', 'content': 'Условные операторы позволяют выполнять разные блоки кода.', 'order': 3, 'quiz_question': 'Ключевое слово условия?', 'quiz_answer': 'if', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Циклы for и while', 'content': 'Циклы позволяют повторять действия много раз.', 'order': 4, 'quiz_question': 'Как начать цикл?', 'quiz_answer': 'for', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Функции', 'content': 'Функции — блоки кода которые можно вызывать много раз.', 'order': 5, 'quiz_question': 'Ключевое слово функции?', 'quiz_answer': 'def', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 1002,
                    'title': 'Python: списки и словари',
                    'description': 'Работа со структурами данных in Python. Списки, словари, кортежи.',
                    'language': 'python', 'level': 'beginner', 'price': 500,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Списки в Python', 'content': 'Список — упорядоченная коллекция элементов. Создание, добавление, удаление.', 'order': 1, 'quiz_question': 'Как создать пустой список?', 'quiz_answer': '[]', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Словари', 'content': 'Словарь хранит пары ключ-значение. Быстрый поиск по ключу.', 'order': 2, 'quiz_question': 'Как создать пустой словарь?', 'quiz_answer': '{}', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Кортежи и множества', 'content': 'Кортеж — неизменяемый список. Множество — уникальные элементы.', 'order': 3, 'quiz_question': 'Ключевое слово для кортежа?', 'quiz_answer': 'tuple', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 1003,
                    'title': 'ООП в Python',
                    'description': 'Объектно-ориентированное программирование. Классы, объекты, наследование.',
                    'language': 'python', 'level': 'intermediate', 'price': 1200,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Классы и объекты', 'content': 'Класс — шаблон для создания объектов. Объект — экземпляр класса.', 'order': 1, 'quiz_question': 'Ключевое слово для класса?', 'quiz_answer': 'class', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Наследование', 'content': 'Наследование позволяет создавать новые классы на основе существующих.', 'order': 2, 'quiz_question': 'Функция для вызова родителя?', 'quiz_answer': 'super', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Инкапсуляция', 'content': 'Скрытие внутренней реализации класса от внешнего мира.', 'order': 3, 'quiz_question': 'Префикс приватного атрибута?', 'quiz_answer': '__', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 1004,
                    'title': 'Django с нуля',
                    'description': 'Создание веб-приложений на Django. Модели, представления, шаблоны.',
                    'language': 'python', 'level': 'intermediate', 'price': 1500,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Введение в Django', 'content': 'Django — популярный веб-фреймворк на Python. Установка и первый проект.', 'order': 1, 'quiz_question': 'Команда создания проекта Django?', 'quiz_answer': 'startproject', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Модели и база данных', 'content': 'Модели описывают структуру данных. Django автоматически создаёт таблицы.', 'order': 2, 'quiz_question': 'Команда создания миграций?', 'quiz_answer': 'makemigrations', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Представления и URL', 'content': 'Представления обрабатывают запросы и возвращают ответы.', 'order': 3, 'quiz_question': 'Декоратор для авторизации?', 'quiz_answer': 'login_required', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 1005,
                    'title': 'Python для анализа данных',
                    'description': 'Pandas, NumPy, Matplotlib. Анализ и визуализация данных.',
                    'language': 'python', 'level': 'advanced', 'price': 2000,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'NumPy основы', 'content': 'NumPy — библиотека для работы с массивами и математическими операциями.', 'order': 1, 'quiz_question': 'Как импортировать NumPy?', 'quiz_answer': 'import numpy', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Pandas DataFrame', 'content': 'DataFrame — двумерная структура данных как таблица Excel.', 'order': 2, 'quiz_question': 'Как импортировать Pandas?', 'quiz_answer': 'import pandas', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Визуализация данных', 'content': 'Matplotlib и Seaborn для создания графиков и диаграмм.', 'order': 3, 'quiz_question': 'Библиотека для графиков?', 'quiz_answer': 'matplotlib', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 2001,
                    'title': 'JavaScript с нуля',
                    'description': 'Основы JavaScript для начинающих. DOM, события, функции.',
                    'language': 'javascript', 'level': 'beginner', 'price': 0,
                    'image_url': 'https://img.icons8.com/color/96/javascript--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Введение в JS', 'content': 'JavaScript — язык программирования для веба. Работает в браузере.', 'order': 1, 'quiz_question': 'Как вывести в консоль JS?', 'quiz_answer': 'console.log', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Переменные let и const', 'content': 'let — изменяемая переменная. const — константа.', 'order': 2, 'quiz_question': 'Как объявить константу?', 'quiz_answer': 'const', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Функции и стрелки', 'content': 'Обычные функции и стрелочные функции () => {}.', 'order': 3, 'quiz_question': 'Символ стрелочной функции?', 'quiz_answer': '=>', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Массивы и методы', 'content': 'map, filter, reduce — мощные методы работы с массивами.', 'order': 4, 'quiz_question': 'Метод фильтрации массива?', 'quiz_answer': 'filter', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'DOM и события', 'content': 'DOM — объектная модель документа. Управляем HTML через JS.', 'order': 5, 'quiz_question': 'Метод поиска элемента по ID?', 'quiz_answer': 'getElementById', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 2002,
                    'title': 'React для начинающих',
                    'description': 'Изучите React с нуля. Компоненты, хуки, состояние.',
                    'language': 'javascript', 'level': 'intermediate', 'price': 1800,
                    'image_url': 'https://img.icons8.com/color/96/react-native.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Что такое React', 'content': 'React — библиотека для создания пользовательских интерфейсов от Facebook.', 'order': 1, 'quiz_question': 'Кто создал React?', 'quiz_answer': 'facebook', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Компоненты и JSX', 'content': 'Компоненты — строительные блоки React приложения. JSX — HTML в JS.', 'order': 2, 'quiz_question': 'Расширение файлов React?', 'quiz_answer': 'jsx', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'useState хук', 'content': 'useState позволяет добавить состояние в функциональный компонент.', 'order': 3, 'quiz_question': 'Хук для состояния?', 'quiz_answer': 'useState', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 2003,
                    'title': 'Node.js и Express',
                    'description': 'Бэкенд на JavaScript. REST API, работа с базами данных.',
                    'language': 'javascript', 'level': 'intermediate', 'price': 1600,
                    'image_url': 'https://img.icons8.com/color/96/nodejs.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Введение в Node.js', 'content': 'Node.js — среда выполнения JavaScript на сервере.', 'order': 1, 'quiz_question': 'На чём основан Node.js?', 'quiz_answer': 'v8', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Express фреймворк', 'content': 'Express — минималистичный веб-фреймворк для Node.js.', 'order': 2, 'quiz_question': 'Команда установки Express?', 'quiz_answer': 'npm install express', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'REST API', 'content': 'REST API — архитектурный стиль для создания веб-сервисов.', 'order': 3, 'quiz_question': 'Метод получения данных?', 'quiz_answer': 'get', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 2004,
                    'title': 'TypeScript основы',
                    'description': 'TypeScript — типизированный JavaScript. Интерфейсы, типы, классы.',
                    'language': 'javascript', 'level': 'advanced', 'price': 2200,
                    'image_url': 'https://img.icons8.com/color/96/typescript.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Что такое TypeScript', 'content': 'TypeScript добавляет статическую типизацию в JavaScript.', 'order': 1, 'quiz_question': 'Расширение файлов TypeScript?', 'quiz_answer': 'ts', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Типы данных', 'content': 'string, number, boolean, array, any — основные типы TypeScript.', 'order': 2, 'quiz_question': 'Тип строки в TypeScript?', 'quiz_answer': 'string', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Интерфейсы', 'content': 'Интерфейсы описывают структуру объектов в TypeScript.', 'order': 3, 'quiz_question': 'Ключевое слово интерфейса?', 'quiz_answer': 'interface', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
            {
                'course': {
                    'stepik_id': 1006,
                    'title': 'Алгоритмы на Python',
                    'description': 'Сортировка, поиск, рекурсия. Подготовка к собеседованиям.',
                    'language': 'python', 'level': 'advanced', 'price': 2500,
                    'image_url': 'https://img.icons8.com/color/96/python--v1.png', 
                    'stepik_url': '',
                },
                'lessons': [
                    {'title': 'Сложность алгоритмов', 'content': 'Big O нотация — оценка эффективности алгоритмов.', 'order': 1, 'quiz_question': 'Обозначение сложности?', 'quiz_answer': 'big o', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Сортировка', 'content': 'Пузырьковая сортировка, быстрая сортировка, сортировка слиянием.', 'order': 2, 'quiz_question': 'Самая быстрая сортировка?', 'quiz_answer': 'быстрая', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                    {'title': 'Рекурсия', 'content': 'Рекурсия — функция которая вызывает сама себя.', 'order': 3, 'quiz_question': 'Что такое рекурсия?', 'quiz_answer': 'функция вызывает себя', 'youtube_url': 'https://www.youtube.com/embed/DzI-S5hgqUI'},
                ]
            },
        ]

        for item in data:
            # Используем update_or_create для гарантированного обновления image_url в базе
            course, created = Course.objects.update_or_create(
                stepik_id=item['course']['stepik_id'],
                defaults=item['course']
            )
            if created:
                self.stdout.write(f'  + {course.title} (создан)')
                for lesson_data in item['lessons']:
                    Lesson.objects.create(course=course, **lesson_data)
                self.stdout.write(f'    {len(item["lessons"])} уроков добавлено')
            else:
                self.stdout.write(f'  * {course.title} (данные обновлены)')

        self.stdout.write(self.style.SUCCESS('Готово!'))