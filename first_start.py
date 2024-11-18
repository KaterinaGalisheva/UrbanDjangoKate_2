'''создание нового проекта '''

# заходим в новую папку нового проекта 
# в терминал вводим команду: python -m venv venv 
 
# далее активируем екзешник командой в терминале 
# venv\Scripts\activate

# в комвндной строке терминала в самом начале должна появится надпись (venv)

# скомпоновать библиотека в файл 
# pip freeze > requirements.txt

# распаковка файла с библиотеками
# pip install -r requirements.txt

# установить Django с помощью pip: 
# pip install django

# Создание первого проекта в конце - это имя проекта
# django-admin startproject project

# Создание приложения внутри проекта, в конце - имя приложения на сервере
# python manage.py startapp app

# создать таблицы в базе данных для всех приложений из списка INSTALLED_APPS в папке progect
# cd project
# python manage.py migrate

# фиксация изменений таблиц в базе данных из модуля models, 
# если есть необходимость создания своих таблиц
# python manage.py makemigrations

# заново создать таблицы в базе данных для всех приложений из списка INSTALLED_APPS в папке mysite
# cd progect
# python manage.py migrate

# Создание приложения внутри проекта, в конце - имя приложения на сервере
# python manage.py startapp app
# подключить его в settings.py

# создать папки (в папке с manage.py) templates для шаблонов html и 
# static для визуализации 
# подключить в settings.py
# 'DIRS': [BASE_DIR / 'templates'],
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Запуск сервера для разработки
# python manage.py runserver

# на папку выше
# cd ..






'''Отправка проекта в репозиторий'''

# создать папку с именем '.git'

# инициализация гит
# git init

# добавление файлов в гит папку
# git add .
# git add filename.py.

# Сделайте первый коммит (фиксация изменений)
# git commit -m "Initial commit"

# Настройте удаленный репозиторий
# git remote add origin <URL-удаленного-репозитория>

# Отправьте изменения в удаленный репозиторий
# git push -u origin master

# Проверьте статус репозитория
# git status


