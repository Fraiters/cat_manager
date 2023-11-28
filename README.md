# cat_manager - Проект Кот Менеджер - Сервис, где зарегистрированные и авторизированные пользователи могут добавлять, удалять, редактировать своих котов. Все пользователи могут просматривать котов.

# cats - пакет взаимодействия с котами

# Модули:

- ## `view.py` - модуль представлений
    - ## Классы:
        - ### `ShowCatList` - Показывает всех загруженных котов
        - ### `ShowCat` - Показывает одного конкретного кота
        - ### `AddCat` - Добавляет кота
        - ### `DeleteCat` - Удаляет кота
        - ### `UpdateCat` - Обновляет кота
        - ### `RegisterUser` - Регистрация пользователя
        - ### `LoginUser` - Авторизация пользователя

- ## `models.py` - модуль с моделями
    - ## Классы:
        - ### `Cat` - Модель Кот (с полями: имя, возраст, порода, вес, фото, описание, автор, slug)
- ## `utils` - вспомогательный модуль
    - ## Классы:
        - ### `CatManagerData` - Класс управления данными Cat
        - ### `ContextMixin` - Миксин формирования контекста для классов представления

- ## `forms` - модуль форм
    - ## Классы:
        - ### `AddCatForm` - Форма добавления кота
        - ### `RegisterUserForm` - Форма регистрации пользователя
        - ### `LoginUserForm` - Форма авторизации пользователя


## Список запросов: 

- ### 'cats/' - Показывает всех загруженных котов
- ### 'cats/add_cat/' - Добавляет кота
- ### 'cats/<slug:cat_slug>/' - Показывает одного конкретного кота
- ### 'cats/<slug:cat_slug>/upd_cat/' - Обновляет кота
- ### 'cats/<slug:cat_slug>/del_cat/' - Удаляет кота

- ### 'register/' - Регистрация пользователя
- ### 'login/' - Авторизация пользователя
- ### 'logout/' - Выход пользователя


# ЗАПУСК:
- ## Локальный запуск: http://127.0.0.1:8000/cats/
- ## Запуск на сервере: https://catmanager-production.up.railway.app/cats/
