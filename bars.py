import json
import sys

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file_json:
        return json.loads(file_json.read())


def get_seats(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_biggest_bar(bars):
    return max(bars, key=get_seats)


def get_smallest_bar(bars):
    return min(bars, key=get_seats)


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar:
                        (bar["geometry"]["coordinates"][0] - longitude) ** 2 +
                        (bar["geometry"]["coordinates"][1] - latitude) ** 2)


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(" Usage:python3 bars.py file path to json")
        exit()
    x_gps = input("longitude:")
    y_gps = input("latitude:")
    while not(is_number(x_gps) and is_number(y_gps)):
        print("You entered incorrect values, enter again")
        x_gps = input("longitude:")
        y_gps = input("latitude:")
    x_gps = float(x_gps)
    y_gps = float(y_gps)
    bars = load_data(sys.argv[1])
    if bars is None:
        exit("data is invalid")
    bars = bars["features"]
    max_bar = get_biggest_bar(bars)
    min_bar = get_smallest_bar(bars)
    near_bar = get_closest_bar(bars, x_gps, y_gps)
    print("\nThe biggest moscow's bar is:")
    print(max_bar["properties"]["Attributes"]["Name"])
    print("\nThe smallest moscow's bar is ")
    print(min_bar["properties"]["Attributes"]["Name"])
    print("\nThe nearest moscow's bar is ")
    print(near_bar["properties"]["Attributes"]["Name"])
