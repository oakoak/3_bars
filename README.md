## Bars

---
This script show the smallest, the largest and the nearest bar
---

### Discription
+ The script show smallest bar from the data array
+ The script show biggest bar
+ The script show nearest bar to **(x,y)**

### Script usage example
```python
import bars
data = bars.load_data(filepath)
print(get_biggest_bar(data))
```
### Also
```python
    get_smallest_bar(bars)
    get_closest_bar(bars, longitude, latitude)
```
When **(longitude, latitude)** - your coordinates


### How starting
```bash
$ python bars.py
```
### Example result
```bash
Biggest bar name: Спорт бар «Красная машина»
Biggest bar address: Автозаводская улица, дом 23, строение 1

Smallest bar name: БАР. СОКИ
Smallest bar address: Дубравная улица, дом 34/29

Nearest bar name: Таверна
Nearest bar address: проспект Защитников Москвы, дом 8

```
##  Where to get data:
    https://devman.org/fshare/1503831681/4/

### Requirements
```bash
Python ver 3.5 (or higher)
```

---

### Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
