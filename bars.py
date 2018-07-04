import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file_json:
            return json.loads(file_json.read())
    except ValueError:
        return None
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


def convert_to_number(str_number):
    try:
        number = float(str_number)
        return number
    except ValueError:
        return None


def get_xy():
    return convert_to_number(input("longitude:")), \
           convert_to_number(input("latitude:"))


def print_bar(bar):
    print(bar["properties"]["Attributes"]["Name"])


def print_information(bars):
    print("\nThe biggest moscow's bar is:")
    print_bar(get_biggest_bar(bars))
    print("\nThe smallest moscow's bar is: ")
    print_bar(get_smallest_bar(bars))
    print("\nThe nearest moscow's bar is: ")
    print_bar(get_closest_bar(bars, x_gps, y_gps))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage:python3 bars.py file path to json")
        records = load_data(sys.argv[1])
    if records is None:
        exit("Could not open file or data is not JSON.")
    bars = records["features"]

    x_gps, y_gps = get_xy()
    if not(x_gps and y_gps):
        exit("You entered incorrect values, enter again.")

    print_information(bars)
