import json


def load_data(filepath):
    file_json = open(filepath, 'r', encoding='utf-8')
    return json.loads(file_json.read())


def get_seats(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_biggest_bar(bars_json):
    return max(bars_json['features'], key=get_seats)


def get_smallest_bar(bars_json):
    return min(bars_json['features'], key=get_seats)


def get_closest_bar(bars_json, longitude, latitude):
    return min(bars_json['features'], key=lambda bar: (bar["geometry"]["coordinates"][0] - longitude) ** 2 +
                                                      (bar["geometry"]["coordinates"][1] - latitude) ** 2)


if __name__ == '__main__':
    x_gps = float(input("longitude:"))
    y_gps = float(input("latitude:"))
    data = load_data("bars.json")
    if data is None :
        exit("data is invalid")
    max_bar = get_biggest_bar(data)
    min_bar = get_smallest_bar(data)
    near_bar = get_closest_bar(data, x_gps, y_gps)
    print("\nThe biggest moscow's bar is:")
    print(max_bar)
    print("\nThe smallest moscow's bar is ")
    print(min_bar)
    print("\nThe nearest moscow's bar is ")
    print(near_bar)