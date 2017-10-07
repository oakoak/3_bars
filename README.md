# Ближайшие бары

Модуль позволяет выяснить какой бар самый мальнький или самый большой, а так же наиблизжащий к вам

# Как использовать

    load_data(filepath)

 Возвращает массив баров из ващего json файла с ними, на вход подается

    get_biggest_bar(bars_json)

Принимает на вход словарь с двумя полями, внутри которого нас интересует поле "features", внутри которого массив с барами. Возвращает словарь с данными наибольшего бара.

    get_smallest_bar(bars_json)

Тоже самое, что и (inline) get_biggest_bar. Возвращает бар с наименьшим количеством сидячих мест

    get_closest_bar(bars_json, longitude, latitude)

Возвращает близжайщий бар к точке (inline)(longitude, latitude)


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
