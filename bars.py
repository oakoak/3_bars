import json
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file_json:
        data_bars = json.loads(file_json.read())
    return data_bars["features"]


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


def get_user_gps():
    try:
        longitube = float(input('Input GPS coordinates longitube: '))
        latitube = float(input('Input GPS coordinates latitube: '))
        return [longitube, latitube]
    except ValueError:
        return None


def print_bar(bar, pointer):
    print("{0} bar name: {1}\n"
          "{0} bar address: {2}\n".format(
            pointer,
            bar["properties"]["Attributes"]["Name"],
            bar["properties"]["Attributes"]["Address"]))


def main():
    try:
        file_path = sys.argv[1]
        bars = load_data(file_path)
    except IndexError:
        exit("Error: No filename for reading!")
    except FileNotFoundError:
        exit("Error: file or path '{0}' not found!\n".format(file_path))
    except json.JSONDecodeError:
        exit("Error: this is not json-file!")

    gps_coordinates = get_user_gps()
    if gps_coordinates:
        print_bar(get_biggest_bar(bars), "Biggest")
        print_bar(get_smallest_bar(bars), "Smallest")
        print_bar(get_closest_bar(bars, gps_coordinates[0], gps_coordinates[1]), "Nearest")
    else:
        exit("Error: GPS coordinates must be input and float type!")


if __name__ == "__main__":
    main()
