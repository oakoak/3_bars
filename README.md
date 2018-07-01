# Ближайшие бары

Модуль позволяет выяснить какой бар самый мальнький или самый большой, а так же наиблизжащий к вам

## Как использовать
```bash
import bars
data = bars.load_data(filepath)
print(get_biggest_bar(data))
```
###Аналогично
```bash
    get_smallest_bar(bars)
    get_closest_bar(bars, longitude, latitude)
```
Где **(longitude, latitude)** - ваши координаты


## Как запустить
```bash
$ python bars.py
Спорт бар «Красная машина»
```
##где взять данные:
    https://devman.org/fshare/1503831681/4/

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
