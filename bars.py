import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file_json:
            return json.loads(file_json.read())
    except IOError:
        return None


def get_seats(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_biggest_bar(bars):
    return max(bars, key=get_seats)


def get_smallest_bar(bars):
    return min(bars, key=get_seats)


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar: (
            (bar["geometry"]["coordinates"][0] - longitude) ** 2 +
            (bar["geometry"]["coordinates"][1] - latitude) ** 2))


def is_number(number):
    try:
        float(number)
        return float(number)
    except ValueError:
        return None


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage:python3 bars.py file path to json.")
    bars = load_data(sys.argv[1])
    if bars is None:
        exit("Could not open file or data is invalid.")
    bars = bars["features"]

    x_gps = is_number(input("longitude:"))
    y_gps = is_number(input("latitude:"))
    if not(x_gps and y_gps):
        exit("You entered incorrect values, enter again.")

    print("\nThe biggest moscow's bar is:")
    print(get_name(get_biggest_bar(bars)))
    print("\nThe smallest moscow's bar is: ")
    print(get_name(get_smallest_bar(bars)))
    print("\nThe nearest moscow's bar is: ")
    print(get_name(get_closest_bar(bars, x_gps, y_gps)))
