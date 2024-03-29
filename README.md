Проект для раздачи векторов
==========================
Состоит из примитивного сервиса по раздаче векторов и библиотеки для работы 
с этим сервисом. 

Также для демонстрационных целей в проекте есть приложение main, которое
выполняет демо-запрос. 

Т.к. файл с векторами большой и для его загрузки требуется много памяти
(и времени), предусмотрена возможность запустить сервис с меньшим количеством
векторов. При этом нужно использовать те слова, которые попали в лимит (в
демо-приложении можно заменить вызов `_data_from_full_set()` на 
`_data_from_short_set()`). 

API
---
**GET**: `<host>/vectors/`

**params**: `word` (url_encoded, пробелы кодируются плюсами) 

Ручка, которая отдает вектора в формате json. В случае отсутствия слова в данных,
возвращает ответ со статусом 404.

Библиотека для работы с апи
---------------------------
Библиотека находится в папке `vector_api_folder`, ее можно установить либо
`pip install git+https://...&subdirectory=vector_api_folder`, либо собрать из 
этой директории пип-модуль. Можно поставить и напрямую из этой папки, как и 
сделано в этом проекте. Библиотека не обрабатывает возможый ответ 404 от сервиса
векторов. 

Установка
---------
1) git clone ...
1) pip install -r requirements.txt

Настройка
---------
Отредактировать в файле settings.py:

`LIMIT = None`

Устанавливает количество строк, которые нужно прочитать из файла. `None` 
обозначает, что лимита нет, и будет прочитан весь файл. В случае установки
лимита, нужно запрашивать слова, которые попали в такой лимит. 

`VEC_LOCATION = '/Users/dtv/Downloads/cc.ru.300.vec'`

Путь к файлу с векторами.

`VEC_API_URL = 'http://localhost:9876/vectors/'`

Путь к ручке, раздающей вектора. 

Запуск
------
```bash
cd raif
./manage.py runserver 0.0.0.0:9876
```
Можно перейти по урл `http://localhost:9876/main/` для того, чтобы посмотреть 
демо-приложение, можно запрашивать вектора для отдельных слов:
`http://localhost:9876/vectors/?word=xxx` 


