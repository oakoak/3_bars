import json


def load_data(filepath):
    file_json = open(filepath, 'r')
    return json.loads(file_json.read())

        
def get_biggest_bar(bars_json):
    return max(bars_json['features'], 
        key = lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars_json):
    return min(bars_json['features'], 
        key = lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars_json, longitude, latitude):
    def distance(bar):
        return ((bar["geometry"]["coordinates"][0] - longitude)**2 +
                (bar["geometry"]["coordinates"][1] - latitude)**2)
    return min(bars_json['features'], key = distance)


if __name__ == '__main__':
    pass