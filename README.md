## Bars

---
This script show the smallest, the largest and the nearest bar
---

### Discription
+ The script show smallest bar from the data array
+ The script show biggest bar
+ The script show nearest bar to **(x,y)**

### script usage example
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
The biggest moscow's bar is:
{'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

The smallest moscow's bar is 
{'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

The nearest moscow's bar is 
{'geometry': {'coordinates': [37.92096900029184, 55.69988800002597], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'af3820bd-14ca-4a68-870d-a3c743e28819', 'Attributes': {'global_id': 281494732, 'Name': 'Таверна', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Юго-Восточный административный округ', 'District': 'район Некрасовка', 'Address': 'проспект Защитников Москвы, дом 8', 'PublicPhone': [{'PublicPhone': '(977) 511-73-23'}], 'SeatsCount': 16, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

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
